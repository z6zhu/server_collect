# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.http import HttpResponseRedirect  
from django.http.response import HttpResponse 
from django.http import HttpResponse 
from django.template import loader, Context
from django.core.urlresolvers import reverse
import json,re,csv,sys
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from models import DevopsRegister,ClientInfo,UpdateTestServer,TestServer,OnlineServer,ZcellModule,ModuleDetail
import datetime
# reload(sys)
# sys.setdefaultencoding('utf8')

pattern=re.compile(r'\n' )
pattern1=re.compile(r'\s+' )

# Create your views here.
@csrf_exempt  
def index(request):
    username = request.session.get('username','anybody')  
    if username=="anybody":
        return redirect(reverse(login))
    else:
        return render(request, 'index.html',{"username":username})
#-------------------------------------------------------------------------------------------------
@csrf_exempt 
def client_account(request):

    if request.method == 'POST' and request.POST:
        phone=request.POST.get('phone')
        add=request.POST.get('add')
        pas=request.POST.get('pas')
        update_id=request.POST.get('update_id')
        if phone and add and pas:
            ClientInfo.objects.create(address=add,phone=phone,password=pas)
    if request.method == 'GET' and request.GET.get('pk_id'):
        ClientInfo.objects.filter(id=request.GET.get('pk_id')).delete()
            
    contact_list = ClientInfo.objects.all()
   
    if request.method == 'GET':
        if request.GET.get('input_value'): 
            contact_list=ClientInfo.objects.filter(address__contains=request.GET.get('input_value'))
            paginator = Paginator(contact_list,10)

            if request.GET.get('page'):
                page = int(request.GET.get('page'))
                if page<1:
                    prev_pager = 0
                    page=1
                    next_pager = 2
                elif page>=paginator.num_pages:
                    prev_pager = paginator.num_pages-1
                    page=paginator.num_pages
                    next_pager =paginator.num_pages
                else:   
                    prev_pager = page -1
                    next_pager = page +1    
                try:
                    contacts = paginator.page(page)
                except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                    contacts = paginator.page(1)
                except EmptyPage:
                # If page is out of range (e.g. 9999), deliver slast page of results.
                    contacts = paginator.page(paginator.num_pages)
                    return render(request,'client_account.html', {"info": contacts,"page":page,"prev_pager":prev_pager,"next_pager":next_pager,"num_pages":paginator.num_pages,"input_info":request.GET.get('input_value')})
             
            return render(request,'client_account.html', {"info": contact_list[:10],"page":1,"prev_pager":0,"next_pager":2,"num_pages":paginator.num_pages,"input_info":request.GET.get('input_value')})
        else:
            paginator = Paginator(contact_list,10)
            if request.GET.get('page'):
                
                page = int(request.GET.get('page'))
        
                if page<1:
                    prev_pager = 0
                    page=1
                    next_pager = 2
                elif page>=paginator.num_pages:
                    prev_pager = paginator.num_pages-1
                    page=paginator.num_pages
                    next_pager =paginator.num_pages
                else:   
                    prev_pager = page -1
                    next_pager = page +1    
                try:
                    contacts = paginator.page(page)
                except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                    contacts = paginator.page(1)
                except EmptyPage:
                # If page is out of range (e.g. 9999), deliver slast page of results.
                    contacts = paginator.page(paginator.num_pages)
             
                return render(request,'client_account.html', {"info": contacts,"page":page,"prev_pager":prev_pager,"next_pager":next_pager,"num_pages":paginator.num_pages})
    
    return render(request,'client_account.html', {"info": contact_list[:10],"page":1,"prev_pager":0,"next_pager":2,"num_pages":paginator.num_pages})
@csrf_exempt     
def online_server(request):
    if request.method == 'POST' and request.POST:
        instance_ID=request.POST.get('instance_ID')
        instance_name=request.POST.get('instance_name')
        out_net=request.POST.get('out_net')
        inner_net=request.POST.get('inner_net')
        deadtime=request.POST.get('deadtime')
        username=request.POST.get('username')
        password=request.POST.get('password')
        SYS=request.POST.get('SYS')
        project=request.POST.get('project')
        
        entry_ID=request.POST.get('entry_ID')
        
        if entry_ID is not None:
            project=re.sub(pattern1,"", project)
            OnlineServer.objects.filter(id=entry_ID).update(instance_id=instance_ID,instance_name=instance_name,out_net=out_net,inner_net=inner_net,deadtime=deadtime,\
                                 username=username,password=password,sys=SYS,project=project)
        else:
            project=re.sub(pattern1,"", project)
            OnlineServer.objects.create(instance_id=instance_ID,instance_name=instance_name,out_net=out_net,inner_net=inner_net,deadtime=deadtime,\
                                 username=username,password=password,sys=SYS,project=project)
    if request.method == 'GET' and request.GET.get('pk_id'):    
        OnlineServer.objects.filter(id=int(request.GET.get('pk_id'))).delete()
    
    contact_list=OnlineServer.objects.all()   
    if request.method == 'GET' and request.GET.get('input_value'): 
        # just support  out_net and project 
        contact_list=OnlineServer.objects.filter(out_net__contains=request.GET.get('input_value'))
        if contact_list.count()==0:
            contact_list=OnlineServer.objects.filter(project__contains=request.GET.get('input_value'))
        
    return render(request, 'online_server.html',{'info':contact_list,'input_info':request.GET.get('input_value')})
    
@csrf_exempt 
def test_server(request):
    if request.method == 'POST' and request.POST:
        instance_ID=request.POST.get('instance_ID')
        instance_name=request.POST.get('instance_name')
        out_net=request.POST.get('out_net')
        inner_net=request.POST.get('inner_net')
        deadtime=request.POST.get('deadtime')
        username=request.POST.get('username')
        password=request.POST.get('password')
        SYS=request.POST.get('SYS')
    
        project=request.POST.get('project')
        
        entry_ID=request.POST.get('entry_ID')
        
        if entry_ID is not None:
            project=re.sub(pattern1,"", project)
            TestServer.objects.filter(id=entry_ID).update(instance_id=instance_ID,instance_name=instance_name,out_net=out_net,inner_net=inner_net,deadtime=deadtime,\
                                 username=username,password=password,sys=SYS,project=project)
        else:
            project=re.sub(pattern1,"", project)
            TestServer.objects.create(instance_id=instance_ID,instance_name=instance_name,out_net=out_net,inner_net=inner_net,deadtime=deadtime,\
                                 username=username,password=password,sys=SYS,project=project)
    if request.method == 'GET' and request.GET.get('pk_id'):    
        TestServer.objects.filter(id=int(request.GET.get('pk_id'))).delete()
    
    contact_list=TestServer.objects.all()   
    if request.method == 'GET' and request.GET.get('input_value'): 
        # just support  out_net and project 
        contact_list=TestServer.objects.filter(out_net__contains=request.GET.get('input_value'))
        if contact_list.count()==0:
            contact_list=TestServer.objects.filter(project__contains=request.GET.get('input_value'))
        
    return render(request, 'test_server.html',{'info':contact_list,'input_info':request.GET.get('input_value')})
@csrf_exempt 
def windows_server(request):
    
    if request.method == 'POST':
        
        if request.POST.get('zone') and request.POST.get('company_id') and request.POST.get('company_name'):
        
            zone=request.POST.get('zone')
            company_id=request.POST.get('company_id')
            company_name=request.POST.get('company_name')
            server_ip=request.POST.get('server_ip')
            server_name=request.POST.get('server_name')
            node=request.POST.get('node')
            passwd=request.POST.get('passwd')
            module_name=request.POST.get('module_name')
            port=request.POST.get('port')
            portv=request.POST.get('portv')
            
            if request.POST.get('module_id'):
                ZcellModule.objects.filter(id=request.POST.get('module_id')).update(id=request.POST.get('module_id'),passwd=passwd,zone=zone,company_id=company_id,company_name=company_name,server_ip=server_ip,server_name=server_name,node=node,module_name=module_name,port=port,portv=portv)
            else:
                ZcellModule.objects.create(passwd=passwd,zone=zone,company_id=company_id,company_name=company_name,server_ip=server_ip,server_name=server_name,node=node,module_name=module_name,port=port,portv=portv)
        
        if request.POST.get('module_entry') and request.POST.get('company_id_entry') and request.POST.get('module_in_entry'):
            
            module=request.POST.get('module_entry')
            company_id=request.POST.get('company_id_entry')
            module_in=request.POST.get('module_in_entry')
            module_version=request.POST.get('module_version_entry')
            module_date=request.POST.get('module_date_entry')
            module_update=request.POST.get('module_update_entry')
            additional=request.POST.get('additional_entry')
            
            if request.POST.get('update_id'):
                ModuleDetail.objects.filter(id=request.POST.get('update_id')).update(id=request.POST.get('update_id'),module=module,module_version=module_version,module_date=module_date,module_update=module_update,additional=additional,module_in=module_in,company_id=company_id)
            else:
                ModuleDetail.objects.create(module=module,module_version=module_version,module_date=module_date,module_update=module_update,additional=additional,module_in=module_in,company_id=company_id)
    
    if request.method == 'GET' and request.GET.get('pk_id'):
        temp=ZcellModule.objects.filter(id=int(request.GET.get('pk_id')))
        if temp.count()!=0:
            ModuleDetail.objects.filter(module__contains=temp[0].module_name).filter(company_id__contains=temp[0].company_id).delete()
            ZcellModule.objects.filter(id=int(request.GET.get('pk_id'))).delete()
            
    if request.method == 'GET' and request.GET.get('detail_id'):     
        ModuleDetail.objects.filter(id=int(request.GET.get('detail_id'))).delete()  
            
    contact_list=ZcellModule.objects.all()
    contact= ModuleDetail.objects.all()
    
    if request.method == 'GET' and request.GET.get('input_value'):
        from django.db.models import Q
        
        #contact_list=ZcellModule.objects.filter(company_name__contains=request.GET.get('input_value'))
        
        contact_list=ZcellModule.objects.filter( Q(company_name__contains=request.GET.get('input_value')) | Q(zone__contains=request.GET.get('input_value')) | Q(company_id__contains=request.GET.get('input_value')) | Q(server_ip__contains=request.GET.get('input_value')) \
                                                | Q(server_name__contains=request.GET.get('input_value')) | Q(node__contains=request.GET.get('input_value')) | Q(node__contains=request.GET.get('input_value')) | Q(module_name__contains=request.GET.get('input_value')))
    
    return render(request, 'windows_server.html',{"info":contact_list,"infomation":contact,"zero_b":request.GET.get('input_value')})
@csrf_exempt 
def test_fresh(request):
    pattern=re.compile(ur' ' )
# -----------------------------add-------------------------------------------    
    if request.method == 'POST' and request.POST:
        
        update_people=request.POST.get('update_people')
        server=request.POST.get('server')
        module=request.POST.get('module')
        sys_variety=request.POST.get('sys_class')
        update_time=request.POST.get('update_time')
        online_offline=request.POST.get('online_offline')
        
        except_info=request.POST.get('except_info')

        update_id=request.POST.get('update_id')
       
        if update_people and server and module and sys_variety  and online_offline: 
# -----------------------------update-------------------------------------------
            if update_id is not None:
                except_info=re.sub(pattern1,"", except_info)
                UpdateTestServer.objects.filter(id=int(update_id)).update(online_offline=online_offline,id=update_id,update_people=update_people,server=server,module=module,sys_variety=sys_variety,update_time=update_time,except_info=except_info)
               
            else:
                time1=datetime.datetime.now()
                update_time=datetime.datetime.strftime(time1,'%Y-%m-%d %H:%M')
                # add T string 
                update_time=re.sub(pattern,"T", update_time)
                except_info=re.sub(pattern1,"", except_info)
                UpdateTestServer.objects.create(online_offline=online_offline,update_people=update_people,server=server,module=module,sys_variety=sys_variety,update_time=update_time,except_info=except_info)
# -----------------------------delete-------------------------------------------
    if request.method == 'GET' and request.GET.get('pk_id'):
        
        UpdateTestServer.objects.filter(id=int(request.GET.get('pk_id'))).delete()
        
    if request.method == 'GET' and request.GET.get('download')=="yes":
        
        if request.GET.get('time_name') and request.GET.get('time_name_right'):
            down_data1=UpdateTestServer.objects.filter(update_time__gte=request.GET.get('time_name'),update_time__lte=request.GET.get('time_name_right'))
        else:
            down_data1=UpdateTestServer.objects.all()
            
        if request.GET.get('module_name'):
         
            down_data2=down_data1.filter(module__contains=request.GET.get('module_name'))    
        else:
            down_data2=down_data1
        
        if request.GET.get('update_people') and request.GET.get('update_people')!="all":
         
            down_data3=down_data2.filter(update_people__contains=request.GET.get('update_people'))
        else:
            down_data3=down_data2
            
        if request.GET.get('online_offline') and request.GET.get('online_offline')!="all":
    
            down_data4=down_data3.filter(online_offline__contains=request.GET.get('online_offline'))
        else:
            down_data4=down_data3
            
        down_data4=down_data4.order_by("-id")
       
   
            
        import csv
        response = HttpResponse(content_type='text/csv')
 
        response['Content-Disposition'] = 'attachment; filename="%s"' %  "server_update_date.csv"        
        writer = csv.writer(response)
        writer.writerow(["线上和测试".encode('GBK'),"项目实施人".encode('GBK'),"服务器名称".encode('GBK'),"更新模块".encode('GBK'),"系统类型".encode('GBK'),"更新时间".encode('GBK'),"更新内容".encode('GBK'),])
        
        for i in down_data4:
            str_1=i.online_offline
            str_2=i.update_people
            str_3=i.server
            str_4=i.module
            str_5=i.sys_variety
            str_6=i.update_time
            str_7=i.except_info.encode('GBK')
            writer.writerow([str_1,str_2,str_3,str_4,str_5,str_6,str_7])
        return response

    
    contact_list=UpdateTestServer.objects.all().order_by("-id")

    paginator = Paginator(contact_list, 10)
# -----------------------------select-------------------------------------------
    if request.method == 'GET':
        dic_val=dict() 
        
        if request.GET.get('time_name') and request.GET.get('time_name_right'):
            dic_val["first_b_right"]=request.GET.get('time_name_right')
            dic_val["first_b"]=request.GET.get('time_name')
            back_data1=UpdateTestServer.objects.filter(update_time__gte=request.GET.get('time_name'),update_time__lte=request.GET.get('time_name_right'))
        else:
            back_data1=UpdateTestServer.objects.all()
            
        if request.GET.get('module_name'):
            dic_val["second_b"]=request.GET.get('module_name')
            back_data2=back_data1.filter(module__contains=request.GET.get('module_name'))    
        else:
            back_data2=back_data1
        
        if request.GET.get('update_people') and request.GET.get('update_people')!="all":
            dic_val["third_b"]=request.GET.get('update_people')
            back_data3=back_data2.filter(update_people__contains=request.GET.get('update_people'))
        else:
            back_data3=back_data2
            
        if request.GET.get('online_offline') and request.GET.get('online_offline')!="all":
            dic_val["zero_b"]=request.GET.get('online_offline')
            back_data4=back_data3.filter(online_offline__contains=request.GET.get('online_offline'))
        else:
            back_data4=back_data3
            
        contact_list=back_data4.order_by("-id")
        paginator = Paginator(contact_list, 10)
        if request.GET.get('page'):

            page = int(request.GET.get('page'))
  
            if page<1:
                prev_pager = 0
                page=1
                next_pager = 2
            elif page>=paginator.num_pages:
                prev_pager = paginator.num_pages-1
                page=paginator.num_pages
                next_pager =paginator.num_pages
            else:   
                prev_pager = page -1
                next_pager = page +1    
            try:
                contacts = paginator.page(page)
            except PageNotAnInteger:
                contacts = paginator.page(1)
            except EmptyPage:
                contacts = paginator.page(paginator.num_pages)
                
            return render(request,'test_fresh.html', {"info": contacts,"page":page,"prev_pager":prev_pager,"next_pager":next_pager,"num_pages":paginator.num_pages,"first_b_right":request.GET.get('time_name_right'),"first_b":request.GET.get('time_name'),"second_b":request.GET.get('module_name'),"third_b":request.GET.get('update_people'),"zero_b":request.GET.get('online_offline')})
 
#         print request.GET.get('time_name')
#         print request.GET.get('time_name_right')
#         print request.GET.get('module_name')
#         print request.GET.get('update_people')
#         print request.GET.get('online_offline')
        dic_val["info"]= contact_list[:10]
        dic_val["page"]= 1
        dic_val["prev_pager"]= 0
        dic_val["next_pager"]= 2
        dic_val["num_pages"]= paginator.num_pages    
        return render(request,'test_fresh.html',dic_val)
    return render(request,'test_fresh.html', {"info": contact_list[:10],"page":1,"prev_pager":0,"next_pager":2,"num_pages":paginator.num_pages})
                                    
#         if request.GET.get('module_name'):
#            
#             if  request.GET.get('time_name') and request.GET.get('time_name_right'):
#             
#                 # ===============datalist had changed
#                 contact_list=UpdateTestServer.objects.filter(update_time__gte=request.GET.get('time_name'),update_time__lte=request.GET.get('time_name_right')).filter(module__contains=request.GET.get('module_name')).order_by("-id")
#                 if request.GET.get('update_people'):
#                     contact_list=UpdateTestServer.objects.filter(update_time__gte=request.GET.get('time_name'),update_time__lte=request.GET.get('time_name_right')).filter(module__contains=request.GET.get('module_name')).filter(update_people__contains=request.GET.get('update_people')).order_by("-id")
#                 # breakpoint  to test the  question-----------
# #                 if request.GET.get('online_offline'):
# #                     contact_list=UpdateTestServer.objects.filter(update_time__gte=request.GET.get('time_name'),update_time__lte=request.GET.get('time_name_right')).filter(module__contains=request.GET.get('module_name')).filter(update_people__contains=request.GET.get('update_people')).filter(online_offline__contains=request.GET.get('online_offline')).order_by("-id")
#                 if request.GET.get('online_offline'):
#                     contact_list=UpdateTestServer.objects.filter(update_time__gte=request.GET.get('time_name'),update_time__lte=request.GET.get('time_name_right')).filter(module__contains=request.GET.get('module_name')).filter(update_people__contains=request.GET.get('update_people')).filter(online_offline__contains=request.GET.get('online_offline')).order_by("-id")
#                 paginator = Paginator(contact_list, 10)
#                 if request.GET.get('page'):
#        
#                     page = int(request.GET.get('page'))
#              
#                     if page<1:
#                         prev_pager = 0
#                         page=1
#                         next_pager = 2
#                     elif page>=paginator.num_pages:
#                         prev_pager = paginator.num_pages-1
#                         page=paginator.num_pages
#                         next_pager =paginator.num_pages
#                     else:   
#                         prev_pager = page -1
#                         next_pager = page +1    
#                     try:
#                         contacts = paginator.page(page)
#                     except PageNotAnInteger:
#                         contacts = paginator.page(1)
#                     except EmptyPage:
#                         contacts = paginator.page(paginator.num_pages)
#                     return render(request,'test_fresh.html', {"info": contacts,"page":page,"prev_pager":prev_pager,"next_pager":next_pager,"num_pages":paginator.num_pages,"first_b_right":request.GET.get('time_name_right'),"first_b":request.GET.get('time_name'),"second_b":request.GET.get('module_name'),"third_b":request.GET.get('update_people'),"zero_b":request.GET.get('online_offline')})
#                 
#                 return render(request,'test_fresh.html', {"info": contact_list[:10],"page":1,"prev_pager":0,"next_pager":2,"num_pages":paginator.num_pages,"first_b_right":request.GET.get('time_name_right'),"first_b":request.GET.get('time_name'),"second_b":request.GET.get('module_name'),"third_b":request.GET.get('update_people'),"zero_b":request.GET.get('online_offline')})
#             else : 
#                 # ===============datalist had changed
#                 contact_list=contact_list=UpdateTestServer.objects.filter(module__contains=request.GET.get('module_name')).order_by("-id")
#                 if request.GET.get('update_people'):
#                     contact_list=UpdateTestServer.objects.filter(module__contains=request.GET.get('module_name')).filter(update_people__contains=request.GET.get('update_people')).order_by("-id")
#                 if request.GET.get('online_offline'):
#                     contact_list=UpdateTestServer.objects.filter(module__contains=request.GET.get('module_name')).filter(update_people__contains=request.GET.get('update_people')).filter(online_offline__contains=request.GET.get('online_offline')).order_by("-id")
#                     
#                 paginator = Paginator(contact_list, 10)
#                 if request.GET.get('page'):
#        
#                     page = int(request.GET.get('page'))
#              
#                     if page<1:
#                         prev_pager = 0
#                         page=1
#                         next_pager = 2
#                     elif page>=paginator.num_pages:
#                         prev_pager = paginator.num_pages-1
#                         page=paginator.num_pages
#                         next_pager =paginator.num_pages
#                     else:   
#                         prev_pager = page -1
#                         next_pager = page +1    
#                     try:
#                         contacts = paginator.page(page)
#                     except PageNotAnInteger:
#                         contacts = paginator.page(1)
#                     except EmptyPage:
#                         contacts = paginator.page(paginator.num_pages)
#                     return render(request,'test_fresh.html', {"info": contacts,"page":page,"prev_pager":prev_pager,"next_pager":next_pager,"num_pages":paginator.num_pages,"first_b_right":request.GET.get('time_name_right'),"first_b":request.GET.get('time_name'),"second_b":request.GET.get('module_name'),"third_b":request.GET.get('update_people'),"zero_b":request.GET.get('online_offline')})
#                 
#                 return render(request,'test_fresh.html', {"info": contact_list[:10],"page":1,"prev_pager":0,"next_pager":2,"num_pages":paginator.num_pages,"first_b_right":request.GET.get('time_name_right'),"first_b":request.GET.get('time_name'),"second_b":request.GET.get('module_name'),"third_b":request.GET.get('update_people'),"zero_b":request.GET.get('online_offline')})
#                
#         else: 
#             
#             if request.GET.get('time_name') and request.GET.get('time_name_right'):
#                 # ===============datalist had changed
#                 
#                 
#                 contact_list=UpdateTestServer.objects.filter(update_time__gte=request.GET.get('time_name'),update_time__lte=request.GET.get('time_name_right')).order_by("-id")
#                 if request.GET.get('update_people'):
#                     contact_list=UpdateTestServer.objects.filter(update_time__gte=request.GET.get('time_name'),update_time__lte=request.GET.get('time_name_right')).filter(update_people__contains=request.GET.get('update_people')).order_by("-id")
# #                 if request.GET.get('update_people'):
# #                     contact_list=UpdateTestServer.objects.filter(update_time__gte=request.GET.get('time_name'),update_time__lte=request.GET.get('time_name_right')).filter(module__contains=request.GET.get('update_people')).order_by("-id")
#                 if request.GET.get('online_offline'):
#                     contact_list=UpdateTestServer.objects.filter(update_time__gte=request.GET.get('time_name'),update_time__lte=request.GET.get('time_name_right')).filter(update_people__contains=request.GET.get('update_people')).filter(online_offline__contains=request.GET.get('online_offline')).order_by("-id")
#                 
#                 paginator = Paginator(contact_list, 10)
#                 if request.GET.get('page'):
#        
#                     page = int(request.GET.get('page'))
#              
#                     if page<1:
#                         prev_pager = 0
#                         page=1
#                         next_pager = 2
#                     elif page>=paginator.num_pages:
#                         prev_pager = paginator.num_pages-1
#                         page=paginator.num_pages
#                         next_pager =paginator.num_pages
#                     else:   
#                         prev_pager = page -1
#                         next_pager = page +1    
#                     try:
#                         contacts = paginator.page(page)
#                     except PageNotAnInteger:
#                         contacts = paginator.page(1)
#                     except EmptyPage:
#                         contacts = paginator.page(paginator.num_pages)
#                     return render(request,'test_fresh.html', {"info": contacts,"page":page,"prev_pager":prev_pager,"next_pager":next_pager,"num_pages":paginator.num_pages,"first_b_right":request.GET.get('time_name_right'),"first_b":request.GET.get('time_name'),"second_b":request.GET.get('module_name'),"third_b":request.GET.get('update_people'),"zero_b":request.GET.get('online_offline')})
#                 
#                 return render(request,'test_fresh.html', {"info": contact_list[:10],"page":1,"prev_pager":0,"next_pager":2,"num_pages":paginator.num_pages,"first_b_right":request.GET.get('time_name_right'),"first_b":request.GET.get('time_name'),"second_b":request.GET.get('module_name'),"third_b":request.GET.get('update_people'),"zero_b":request.GET.get('online_offline')})
#                 
#             else:
#                 if request.GET.get('update_people'):
#                     print '------------',request.GET.get('update_people')
#                     contact_list=UpdateTestServer.objects.filter(update_people__contains=request.GET.get('update_people')).order_by("-id")
#                     
#                     if request.GET.get('online_offline'):
#                         print '------------',request.GET.get('online_offline')
#                         contact_list=UpdateTestServer.objects.filter(update_people__contains=request.GET.get('update_people')).filter(online_offline__contains=request.GET.get('online_offline')).order_by("-id")
#             
#                         paginator = Paginator(contact_list, 10)
#                         if request.GET.get('page'):
#                             page = int(request.GET.get('page'))
#                        
#                             if page<1:
#                                 prev_pager = 0
#                                 page=1
#                                 next_pager = 2
#                             elif page>=paginator.num_pages:
#                                 prev_pager = paginator.num_pages-1
#                                 page=paginator.num_pages
#                                 next_pager =paginator.num_pages
#                             else:   
#                                 prev_pager = page -1
#                                 next_pager = page +1    
#                             try:
#                                 contacts = paginator.page(page)
#                             except PageNotAnInteger:
#                                 contacts = paginator.page(1)
#                             except EmptyPage:
#                                 contacts = paginator.page(paginator.num_pages)
#                             return render(request,'test_fresh.html', {"info": contacts,"page":page,"prev_pager":prev_pager,"next_pager":next_pager,"num_pages":paginator.num_pages,"first_b_right":request.GET.get('time_name_right'),"first_b":request.GET.get('time_name'),"second_b":request.GET.get('module_name'),"third_b":request.GET.get('update_people'),"zero_b":request.GET.get('online_offline')})
#                      
#                         return render(request,'test_fresh.html', {"info": contact_list[:10],"page":1,"prev_pager":0,"00":2,"num_pages":paginator.num_pages,"first_b_right":request.GET.get('time_name_right'),"first_b":request.GET.get('time_name'),"second_b":request.GET.get('module_name'),"third_b":request.GET.get('update_people'),"zero_b":request.GET.get('online_offline')})
#                 else:     
#                     # contact_list use the first =============== contact_list    
#                     if request.GET.get('page'):
#                         page = int(request.GET.get('page'))
#                   
#                         if page<1:
#                             prev_pager = 0
#                             page=1
#                             next_pager = 2
#                         elif page>=paginator.num_pages:
#                             prev_pager = paginator.num_pages-1
#                             page=paginator.num_pages
#                             next_pager =paginator.num_pages
#                         else:   
#                             prev_pager = page -1
#                             next_pager = page +1    
#                         try:
#                             contacts = paginator.page(page)
#                         except PageNotAnInteger:
#                             contacts = paginator.page(1)
#                         except EmptyPage:
#                             contacts = paginator.page(paginator.num_pages)
#                         return render(request,'test_fresh.html', {"info": contacts,"page":page,"prev_pager":prev_pager,"next_pager":next_pager,"num_pages":paginator.num_pages})
#         
#     return render(request,'test_fresh.html', {"info": contact_list[:10],"page":1,"prev_pager":0,"next_pager":2,"num_pages":paginator.num_pages})
 
#-------------------------------------------------------------------------------------------------
@csrf_exempt  
def login(request):
    if request.method == "POST":
        username=request.POST['username']
        pswd=request.POST['pswd']
        if username and pswd:
            obj=DevopsRegister.objects.filter(username=username,passwd=pswd)
            for i in obj:
                if obj!=list():
                    request.session['username'] = username  
                    return redirect('index_page')  # url name                        
    return render(request, 'login.html')
@csrf_exempt  
def logout(request):
    del request.session['username']                   
    return redirect('login_page')
@csrf_exempt  
def register(request):
    register_dict={"1":"pro","2":"dev","3":"review","4":"test","5":"opt","6":"CTO"}
    if request.method == "POST":
        try:
            user=request.POST['username']
            pswd=request.POST['pswd']
            class_num=request.POST['gg']
            class_str=register_dict[class_num]
            if user and pswd and class_str:
                pass
            else:
                raise Exception
        except:           
            return HttpResponseRedirect('/register/')
        else:
            #return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))   
            DevopsRegister.objects.create(username=user,passwd=pswd,role=class_str)
            return HttpResponseRedirect('/login/')          
    return render(request, 'register.html')
@csrf_exempt  
def change_pwd(request):
    if request.method == "POST":
        user=request.POST['username']
        oldpswd=request.POST['oldpswd']
        newpswd=request.POST['newpswd']
        obj=DevopsRegister.objects.filter(username=user,passwd=oldpswd)
        for i in obj:
            if obj!=list() and newpswd:
                DevopsRegister.objects.filter(username=user).update(passwd=newpswd)
                return HttpResponseRedirect('/login/')
            else:
                return HttpResponseRedirect('/change_pwd/')                  
    return render(request, 'change_pwd.html')