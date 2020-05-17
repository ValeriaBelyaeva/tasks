# задача "Узнай друзей своего соседа"
# bdate lists
import vk_api

vk_session = vk_api.VkApi(
    token="4280b1484280b1484280b148c742f1d36e442804280b1481c23e054a681fb2cfca5fea9")

vk = vk_session.get_api()

spisok = [(i, 0) for i in range(100)]
user_id = vk_api.users.get(user_ids="akerzhakov_11",
                    filds="id")
# list_id=friends.getLists
for i in user_id.friends.getLists(order="random",
                          fields="bdate"):
    spisok[i][1] += 1


for i in spisok.sort():
    print(i)