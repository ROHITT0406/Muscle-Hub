from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.models import Contact,Plansdetails,Class
from .serializers import ContactSerializer,ClassSerializer,PlanSerializer



@api_view(['GET','POST','DELETE'])
def contact(request):
    if request.method == "GET":
        objs=Contact.objects.all()
        serializer = ContactSerializer(objs,many= True)
        return Response(serializer.data)
    elif request.method == "POST":
        data=request.data
        serializer=ContactSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    else:
        data=request.data
        obj=Contact.objects.get(id=data['id'])
        obj.delete()
        return Response({'message':'contact deleted'})


@api_view(['GET','DELETE'])
def classes(request):
    if request.method == "GET":
        objs=Class.objects.all()
        serializer = ClassSerializer(objs,many= True)
        return Response(serializer.data)
    else:
        data=request.data

        objs=Class.objects.get(id=data['data'])
        objs.delete()
        return Response({"message":"class deleted"})
    

@api_view(['GET','POST','DELETE','PATCH'])
def plan(request):
    if request.method == "GET":
        objs=Plansdetails.objects.all()
        serializer = PlanSerializer(objs,many= True)
        return Response(serializer.data)
    elif request.method == "POST":
        data=request.data
        serializer=PlanSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method == "PATCH":
        data=request.data
        obj=Plansdetails.objects.get(id=data['id'])
        serializer=PlanSerializer(obj,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    else:
        data=request.data
        obj=Plansdetails.objects.get(id=data['id'])
        obj.delete()
        return Response({'message':'plan deleted'})
    

    
@api_view(['GET'])
def getplan(request,pk):
   try:
        room=Plansdetails.objects.get(id=pk)
        serializer=PlanSerializer(room,many=False)
        return Response(serializer.data)
   except Exception as identifier:
       return Response({"message":"Id not found"})