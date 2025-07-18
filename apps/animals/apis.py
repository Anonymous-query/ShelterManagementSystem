from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from apps.animals.models import Animals, AdoptionRequest
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from apps.animals.serializer import AdoptionRequestSerializer, AnimalSerializer
from django.db.models import Q

class AnimalsList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        """
        Return a list of all animals.
        """
        search_by = request.GET.get('search_by', None)
        filter_by = request.GET.get('filter_by', None)

        if search_by and filter_by:
            animal_objs = Animals.objects.select_related('species', 'breed').filter(
                Q(species__name__contains=search_by) | Q(breed__name__contains=search_by)
            ).order_by(filter_by)
        elif search_by:
            animal_objs = Animals.objects.select_related('species', 'breed').filter(species__name__contains=search_by)
        elif filter_by:
            # order_by_is = {filter_by}'
            animal_objs = Animals.objects.select_related('species', 'breed').all().order_by(filter_by)
        else:
            animal_objs = Animals.objects.select_related('species', 'breed').all()
        animal_serilizer = AnimalSerializer(animal_objs, many=True)

        return Response({'data': animal_serilizer.data, 'status': True}, status=status.HTTP_200_OK)
    

class CustomAPIView(APIView):
    def get_permissions(self):
        # Instances and returns the dict of permissions that the view requires.
        return {key: [permission() for permission in permissions] for key, permissions in self.permission_classes.items()}

    def check_permissions(self, request):
        method = request.method.lower()
        for permission in self.get_permissions()[method]:
            if not permission.has_permission(request, self):
                self.permission_denied(
                    request, message=getattr(permission, 'message', None)
                )

class AnimalAdoptionRequestHandler(CustomAPIView):
    permission_classes = {"get": [permissions.IsAdminUser, permissions.IsAuthenticated], "post": [permissions.IsAuthenticated], 'patch': [permissions.IsAdminUser]}

    def get(self, request, id):
        if id:
            try:
                adoption_request = AdoptionRequest.objects.get(id=id)
            except AdoptionRequest.DoesNotExist:
                 return Response({'message': 'Adoption request does not exist of provide id', 'status': False}, status=status.HTTP_400_BAD_REQUEST)
            serilizer = AdoptionRequestSerializer(adoption_request)
        else:
            adoption_request = AdoptionRequest.objects.all()
            serilizer = AdoptionRequestSerializer(adoption_request, many=True)
        return Response({'result': serilizer.data, 'status': True}, status=status.HTTP_200_OK)

    def post(self, request):
        animal_id = request.POST.get('animal_id', None)
        user = request.user

        if animal_id is None or animal_id == '':
            return Response({'message': 'Animal id required for submiting request', 'status': False}, status=status.HTTP_400_BAD_REQUEST)

        try:
            animal_obj = Animals.objects.get(id=animal_id)
        except Animals.DoesNotExist:
            return Response({'message': 'Animal not found with provide ID', 'status': False}, status=status.HTTP_400_BAD_REQUEST)

        _ = AdoptionRequest.objects.create(
            user=user,
            animal=animal_obj
        )

        return Response({'message': 'Request has been submit for adoption', 'status': True}, status=status.HTTP_201_CREATED)

    def patch(self, request, id):

        request_status = request.POST.get('status')

        if request_status not in ['approved', 'rejected']:
            return Response({'message': 'Adoption request status must be approved or rejected', 'status': False}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            adoption_request = AdoptionRequest.objects.get(id=id)
        except Animals.DoesNotExist:
            return Response({'message': 'Adoption request not found with provide ID', 'status': False}, status=status.HTTP_400_BAD_REQUEST)
        
        adoption_request.status = request_status
        adoption_request.save()

        animal_obj = Animals.objects.get(id=adoption_request.animal.id)
        animal_obj.adoption_status = request_status
        animal_obj.save()

        return Response({'message': f'Adoption request has been granded with {request_status}', 'status': True}, status=status.HTTP_200_OK)