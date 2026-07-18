from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Match, MatchPlayer
from .serializers import MatchSerializer, MatchPlayerSerializer

# logic for how the User can view matches  
class MatchViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = MatchSerializer

    def get_queryset(self):
        return Match.objects.all()
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    
#logic for user registering to the app   
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, password=password, email=email)
    return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)

#logic for user login to the app-not needed; Django REST Framework SimpleJWT provides it

#logic for user joining matches
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def join_match(request, match_id):
    # find the match
    try:
        match = Match.objects.get(id=match_id)
    except Match.DoesNotExist:
        return Response({'error': 'Match not found'}, status=status.HTTP_404_NOT_FOUND)

    # check if match is open
    if match.status != 'open':
        return Response({'error': 'Match is not open for joining'}, status=status.HTTP_400_BAD_REQUEST)

    # check if user already joined
    if MatchPlayer.objects.filter(match=match, player=request.user).exists():
        return Response({'error': 'You already joined this match'}, status=status.HTTP_400_BAD_REQUEST)

    # check if slots available
    current_players = MatchPlayer.objects.filter(match=match).count()
    if current_players >= match.total_slots:
        return Response({'error': 'Match is full'}, status=status.HTTP_400_BAD_REQUEST)

    # join the match
    match_player = MatchPlayer.objects.create(match=match, player=request.user)

    # update status to full if all slots taken
    if current_players + 1 >= match.total_slots:
        match.status = 'full'
        match.save()

    serializer = MatchPlayerSerializer(match_player)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


#logic for user leaving matches
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def leave_match(request, match_id):
    # find the match
    try:
        match = Match.objects.get(id=match_id)
    except Match.DoesNotExist:
        return Response({'error': 'Match not found'}, status=status.HTTP_404_NOT_FOUND)

    # check if user joined
    try:
        match_player = MatchPlayer.objects.get(match=match, player=request.user)
    except MatchPlayer.DoesNotExist:
        return Response({'error': 'You have not joined this match'}, status=status.HTTP_400_BAD_REQUEST)

    # leave the match
    match_player.delete()

    # update status to open if it was full
    if match.status == 'full':
        match.status = 'open'
        match.save()

    return Response({'message': 'You have left the match'}, status=status.HTTP_200_OK)

