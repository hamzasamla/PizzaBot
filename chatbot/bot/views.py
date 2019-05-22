from django.views.generic import TemplateView
from django.shortcuts import render,redirect
import requests

from .forms import MessageForm
from .models import Message

class HomeView(TemplateView):
    template_name='chatbot/chatbot.html'

    def get(self,request):
        form=MessageForm
        chatlog=Message.objects.all()
        args={'form':form,'chatlog':chatlog}
        return render(request,self.template_name,args)

    def post(self,request):
        form=MessageForm(request.POST)
        if form.is_valid():
            msg=form.save(commit=False)

            text=form.cleaned_data['post']
            botRes=text

            msg.message=text
            msg.sender='Me'
            msg.save()

            data={
                "contexts":[
                    "shop"
                ],
                "lang":"en",
                "query":text,
                "sessionId":"12345",
                "timezone":"America/New_York"
            }

            r=requests.post("https://api.dialogflow.com/v1/query?v=20150910",
                    json=data,
                    headers={
                    "Authorization":"Bearer 2aa6a10d207c476fa16f05b69edc493d",
                    "Content-Type":"application/json"
                    }).json()

            botRes=r['result']['fulfillment']['speech']

            reply=Message()
            reply.message=botRes
            reply.sender="PizzaBot"
            reply.save()
            
            form=MessageForm()

        chatlog=Message.objects.all()
        args={'form':form,'chatlog':chatlog}
        return render(request,self.template_name,args)

