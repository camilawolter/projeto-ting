def exists_word(word, instance, contains_info=False):
    files_with_word = []

    for index in range(len(instance)):
        file = instance.search(index)
        lines_word = []
        line_number = 0

        for file_line in file["linhas_do_arquivo"]:
            line_number += 1

            if word.lower() in file_line.lower():
                line_dict = {"linha": line_number, "conteudo": file_line
                             } if contains_info else {"linha": line_number}
                lines_word.append(line_dict)

        if lines_word:
            data = {
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": lines_word
            }
            files_with_word.append(data)

    return files_with_word


def search_by_word(word, instance):
    return exists_word(word, instance, True)
