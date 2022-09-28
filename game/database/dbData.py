def get_user_data(id_user) -> dict:
    list_keyword = ["questions_answered", "points", "polls_answered", "quizs_answered"]
    if __name__ == "__main__":
        file_read = open("userData.txt", "rt")
    else:
        file_read = open("game/database/userData.txt", "rt")

    txt_read = file_read.read()
    dict_data = {
        "questions_answered": None,
        "points": None,
        "polls_answered": None,
        "quizs_answered": None,
    }
    # print("A: " + file_read)
    try:
        for keyword in list_keyword:
            word_to_find = f"{keyword}{id_user}:"
            keyword_search_len = len(word_to_find)
            index_found = txt_read.find(word_to_find)
            cut_from_index = txt_read[index_found:]
            search_the_come = cut_from_index.find(",")

            # para obtener recompensa
            user_data = txt_read[index_found + keyword_search_len: index_found + search_the_come]

            dict_data[keyword] = int(user_data)
    except ValueError:
        print("Function call before of: error=ValueError, file: dbData.py")

    return dict_data
def set_user_data(id_user, keyword, new_value):
    if type(keyword) == dict:
        for key, value in keyword.items():
            modify_data(id_user, key, value)
    else:
        modify_data(id_user, keyword, new_value)

def modify_data(id_user, keyword, new_value):
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
        cut_text_start = info_file[0:index_found + keyword_search_len]
        search_the_come = cut_from_index.find(",")
        cut_text_end = info_file[index_found + search_the_come:]

        info_to_write_file = f"{cut_text_start}{new_value}{cut_text_end}"

        file_write.write(info_to_write_file)
        file_write.close()
