def get_user_id(id_user) -> int:
    if __name__ == "__main__":
        file_read = open("userId.txt", "rt")
    else:
        file_read = open("game/database/userId.txt", "rt")

    txt_read = file_read.read()
    try:
        word_to_find = f"id{id_user}:"
        keyword_search_len = len(word_to_find)
        index_found = txt_read.find(word_to_find)
        cut_from_index = txt_read[index_found:]
        search_the_come = cut_from_index.find(",")

        # para obtener recompensa
        user_id = txt_read[index_found + keyword_search_len: index_found + search_the_come]
        return user_id
    except ValueError:
        print("Function call before of: error=ValueError, file: dbData.py")

    return 0


def set_user_data_id(id_user, keyword, new_value):
    if __name__ == "__main__":
        file_read = open("userId.txt", "rt")
    else:
        file_read = open("game/database/userId.txt", "rt")

    info_file = file_read.read()

    if str(id_user) not in info_file:
        if __name__ == "__main__":
            file_write = open("userId.txt", "a")
        else:
            file_write = open("game/database/userId.txt", "a")

        word_to_find = f"{keyword}{id_user}:{new_value},\n"

        info_to_write_file = word_to_find

        file_write.write(info_to_write_file)
        file_write.close()
