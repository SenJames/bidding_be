# bidding_app/serializers.py
from rest_framework import serializers
from .models import Bid, Staff, Item


class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = ['id', 'item', 'giver', 'time', 'recipient']


class BidEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = ['item', 'giver', 'time', 'recipient', 'time']
