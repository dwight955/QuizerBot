from generalVariable.constant import CONSTANT


def get_user_data(id_user) -> dict:
    list_keyword = ["questions_answered", "points"]
    if __name__ == "__main__":
        file_read = open("userData.txt", "rt")
    else:
        file_read = open("game/database/userData.txt", "rt")

    txt_read = file_read.read()
    dict_data = {
        "questions_answered": None,
        "points": None
    }
    # print("A: " + file_read)
    for keyword in list_keyword:
        word_to_find = f"{keyword}{id_user}:"
        keyword_search_len = len(word_to_find)
        index_found = txt_read.find(word_to_find)
        cut_from_index = txt_read[index_found:]
        search_the_come = cut_from_index.find(",")

        #para obtener recompensa
        user_data = txt_read[index_found+keyword_search_len: index_found+search_the_come]
        # print("Recompensa: " + user_data)
        # print(cut_number)
        dict_data[keyword] = int(user_data)

    # print(dict_data)
    return dict_data
# get_user_data(1822798056)

def set_user_data(id_user, keyword, number_data):
    if __name__ == "__main__":
        file_read = open("userData.txt", "rt")
    else:
        file_read = open("game/database/userData.txt", "rt")

    info_file = file_read.read()
    if str(id_user) in info_file:
        if __name__ == "__main__":
            file_write = open("userData.txt", "w")
        else:
            file_write = open("game/database/userData.txt", "w")

        word_to_find = f"{keyword}{id_user}:"
        keyword_search_len = len(word_to_find)
        index_found = info_file.find(word_to_find)
        cut_from_index = info_file[index_found:]
        cut_text_start = info_file[0:index_found+keyword_search_len]
        search_the_come = cut_from_index.find(",")
        cut_text_end = info_file[index_found+search_the_come:]

        info_to_write_file = f"{cut_text_start}{number_data}{cut_text_end}"
        # print(info_to_write_file)

        file_write.write(info_to_write_file)
        file_write.close()
    else:
        if __name__ == "__main__":
            file_append = open("userData.txt", "a")
        else:
            file_append = open("game/database/userData.txt", "a")

        add_new_user = f"\nquestions_answered{id_user}:0,\npoints{id_user}:0,"
        file_append.write(add_new_user)
        file_append.close()


# set_user_data(1822798056, "questions_answered", 1000)
# set_user_data(1822798056, "points", 111)
# set_user_data(1822728056, "points", 100)
# set_user_data(1822728056, "questions_answered", 163)
# set_user_data(1822798056,"points")
# set_user_data(1822798056,"questions_answered")
