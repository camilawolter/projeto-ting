from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    texts_line = txt_importer(path_file)
    dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(texts_line),
        "linhas_do_arquivo": texts_line
    }

    i = 0
    while (i < len(instance)
           and instance.search(i)["nome_do_arquivo"] != path_file):
        i += 1
    if i >= len(instance):
        instance.enqueue(dict)
        print(dict)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
