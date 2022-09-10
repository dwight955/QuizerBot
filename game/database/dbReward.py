import sys
from generalVariable.constant import CONSTANT
async def save_user(id_user) -> bool:
    file = open("game/database/userReward.txt", "rt")
    info_file = file.read()
    # print("Read: " + info_file)
    if str(id_user) not in info_file:
        print("No esta")
        try:
            files = open("game/database/userReward.txt", "a")
            formate_txt = f"userStart{id_user}:\nuserEnd{id_user}:\n"
            files.write(formate_txt)
        except:
            print("Error file...")
        finally:
            files.close()
    else:
        return False
    return True

file = open("userReward.txt", "rt")
print(file.read())


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

# dataSave("6.rw")
# file = open("userReward.txt", "rt")
# print(file.read())
# print("\n")
# dataSave("7.rw")
# file = open("userReward.txt", "rt")
# print(file.read())
# print("\n")
# dataSave("8.rw")
# file = open("userReward.txt", "rt")
# print(file.read())
# print("\n")
# dataSave("9.rw")
# file = open("userReward.txt", "rt")
# print(file.read())
# print("\n")
# dataSave("10.rw")
# file = open("userReward.txt", "rt")
# print(file.read())

    # file = open("game/database/userReward.txt", "rt")
    # txt = file.read()
    # index_found = txt.find("questions_answered:")
    # keyword_search_len = len("questions_answered:")
    # cut_number = txt[(index_found + keyword_search_len):
    #                  ((index_found + keyword_search_len) + CONSTANT.NUMBER_CHAR_TO_CUT)] #example cut = txt[34:(34+4)]
    # print(int(cut_number))
