def exists_word(word, instance):
    files_with_word = []

    for index in range(len(instance)):
        file = instance.search(index)
        lines_word = []
        line_number = 0

        for line in file["linhas_do_arquivo"]:
            line_number += 1

            if word.lower() in line.lower():
                lines_word.append({"linha": line_number})

        if lines_word:
            data = {
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": lines_word
            }
            files_with_word.append(data)

    return files_with_word


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
