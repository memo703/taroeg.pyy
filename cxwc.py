from xsvt import Client
messsage=""""⠀
[CB] Anime , RolePlay NSFW🫦🔞

[CB] منتدى سكس نيك تعال جلخ🔞

[BC]💌 - amazing Community : 
[BC]
[BC]💌 - منتدى رائع يشرفنا انضمامكم : 
[cb]http://aminoapps.com/c/Tslyh502"""
title="HOT+18"
client = Client(device_key="E7309ECC0953C6FA60005B2765F99DBBC965C8E9",signature_key="DFA5ED192DDA6E88A12FE12130DC6206B1251E44",service_key="ZTFjNjVmNTBkNWY1ZmI0OQ==")
email="kiarauchiha666@gmail.com"
password="kiarabuhid"
client.login(email=email,password=password)
comlink=["http://aminoapps.com/c/Aurorix","http://aminoapps.com/c/Tslyh502","http://aminoapps.com/c/NmyJwhr","http://aminoapps.com/c/MjlsLwtkw"]
for i in comlink:
    w=client.fetch_community_id(i)
    print(w)
    try :
        client.join_community(w)
    except Exception as e:
        print(e)
k=0
v=client.joined_communities().comId
for i in v:
    
    client.set_community_id(community_id=i)
    client.edit_profile(nickname="⋆｡‧˚ʚ🍓فراولةɞ˚‧｡⋆≀ׅᨴ🔥🔞")
    client.edit_profile(content=content)
    content=open("virus.txt").read()
    online=client.community.fetch_online_users().uid
    lea=client.community.fetch_users(userType="CURATORS").userId
    online = [user for user in online if user not in lea]
    cur=client.community.fetch_users(userType="LEADERS").userId
    online = [user for user in online if user not in cur]
    if len(online)<1:
        print("no online in this comunity")
    else:
        try:
            
            a=client.community.start_chat(userIds=online,message=messsage,title=title).chatId
            client.community.send_image(chatId=a,image="https://i.imgur.com/TEMhU2e.jpeg",comId=i)
            a=client.community.start_chat(userIds=online,message=messsage,title=title).chatId 
            client.community.send_image(chatId=a,image="https://i.imgur.com/TEMhU2e.jpeg",comId=i)

        except Exception as e:
            print(e)
        try:
            a=client.start_chat(userId=online,message=messsage,title=title).chatId
        except:
            k=K+1