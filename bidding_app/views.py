from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework import generics
from .models import Bid, Item, Staff
from .serializers import BidSerializer, BidEventSerializer
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status, generics, views
from rest_framework.decorators import api_view


# Create your views here.
# bidding_app/views.py


class BidListCreateView(generics.ListCreateAPIView):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer


class BidList1(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        snippets = Bid.objects.all()
        serializer = BidSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BidSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BidList(generics.ListAPIView):
    """
    List all Bids, or create a new snippet.
    """
    queryset = Bid.objects.all()

    def get(self, request, format=None):
        bids = Bid.objects.all()
        print(bids)

        res = []
        # serializer = BidSerializer(bids, many=True)

        for i in bids:
            data = {}
            data['item'] = i.item.item_name
            data['giver'] = i.giver.username
            data['recipient'] = i.recipient
            data['time'] = i.item.time
            res.append(data)

        # serializer = BidSerializer(bids, many=True)
        # print(serializer.data)
        print(res)
        return Response({'data': res}, status=status.HTTP_200_OK)


class ItemListView(generics.ListAPIView):
    queryset = Item.objects.all()

    def get(self, request, format=None):
        items = Item.objects.all()
        res = []

        for i in items:
            data = {}
            data['name'] = i.item_name
            # data['phone'] = i.item_photo
            data['count'] = i.count
            res.append(data)
            print(res)
        return Response({'data': res}, status=status.HTTP_200_OK)


class BidAction(APIView):
    """
    Create Goals.
    """
    # permission_class = ['IsAuthenticated']
    # authentication_classes = [BasicAuthentication]

    def post(self, request, format=None):
        # collecting data
        # uuid field for owner
        staff = request.data.get('staff')
        item = request.data.get('item')
        receiver = request.data.get('recipient')

        print(request.user)

        # Ensuring that only staff members can bid
        try:
            # Ensuring that only registered owner is the only one who can creaate goals
            bidder = Staff.objects.get(
                user=staff.lower())
            print(bidder)
            if bidder.giver == True:
                gift = Item.objects.get(item_name=item.lower())
                print(gift.count)
                if gift.count > 0:
                    data = {
                        "item": gift.id,
                        "giver": bidder.id,
                        "recipient": receiver
                    }
                    serializer = BidEventSerializer(
                        data=data)
                    if serializer.is_valid():
                        bidEvent = Bid.objects.create(
                            item=gift, giver=bidder, recipient=receiver)
                        bidEvent.save()
                        bidder.giver = False
                        gift.count -= 1
                        bidder.save()
                        gift.save()
                        return Response(data={"item": gift.item_name, "giver": bidder.user, "recipient": serializer.data["recipient"]}, status=status.HTTP_201_CREATED)
                    else:
                        print(serializer.errors)
                        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response(data={'response': f'{gift.item_name} is already gifted to someone'}, status=status.HTTP_410_GONE)
            else:
                return Response(data={'response': f'{bidder.user} you already bidded'}, status=status.HTTP_410_GONE)

        except Exception as E:
            return Response({"error": str(E)},
                            status=status.HTTP_400_BAD_REQUEST)
