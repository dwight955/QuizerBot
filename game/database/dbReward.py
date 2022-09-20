import sys
from generalVariable.constant import CONSTANT
async def save_user(id_user) -> bool:
    file = open("game/database/userReward.txt", "rt")
    info_file = file.read()
    # print("Read: " + info_file)
    if str(id_user) not in info_file:
        print("No esta")
        try:
            file_reward = open("game/database/userReward.txt", "a")
            formate_txt_reward = f"userStart{id_user}:\nuserEnd{id_user}:\n"
            file_reward.write(formate_txt_reward)

            file_data = open("game/database/userData.txt", "a")
            formate_txt_reward = f"questions_answered{id_user}:0,\npoints{id_user}:0,\npolls_answered{id_user}:0,\nquizs_answered{id_user}:0,\n"
            file_data.write(formate_txt_reward)

        except:
            print("Error file...")
        finally:
            file_reward.close()
            file_data.close()
    else:
        return False
    return True

async def data_save(reward, id_user):
    file = open("game/database/userReward.txt", "rt")
    txt = file.read()
    sizeFile = (sys.getsizeof(txt)-49)
    format_start_index = f"userStart{id_user}:"
    format_end_index = f"userEnd{id_user}:"
    indexStart = txt.find(format_start_index)
    indexEnd = txt.find(format_end_index)
    cutTxtStart = txt[0:indexEnd]
    cutTxtEnd = txt[indexEnd:]
    try:
        file = open("game/database/userReward.txt", "w")
        format = cutTxtStart + reward + "\n" + cutTxtEnd
        file.write(format)
    except:
        print("Error file... 1")
    finally:
        file.close()
def get_user_reward(id_user) -> list:
    try:
        file = open("../../game/database/userReward.txt", "rt")
        txt = file.read()
        len_user_reward_start = len(f"userStart{id_user}:")
        format_start_index = f"userStart{id_user}:"
        format_end_index = f"userEnd{id_user}:"
        indexStart = txt.find(format_start_index)
        indexEnd = txt.find(format_end_index)

        cutTxtStart = txt[(indexStart + len_user_reward_start+1):(indexEnd-1)]
        print("Yeah: " + str(cutTxtStart.split("\n")))
    except:
        print("Error al obtener reward del usuario...")

    return cutTxtStart.split("\n")
