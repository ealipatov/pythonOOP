txt = "Значимость этих проблем настолько очевидна, что новая модель организационной деятельности влечет за собой " \
      "процесс внедрения и модернизации позиций, занимаемых участниками в отношении поставленных задач. " \
      "Практический опыт показывает, что постоянное информационно-техническое обеспечение нашей деятельности " \
      "способствует подготовке и реализации позиций, занимаемых участниками в отношении поставленных задач. " \
      "Задача организации, в особенности же дальнейшее..."


def clear_symbol_in_text(symbol):
    def decorator(func):
        def inner(*args, **kwargs):
            print(f"\nТекст без символа: `{symbol}`:")
            valid_args = []
            for arg in args:
                valid_args.append(str(arg).replace(symbol, ""))
            res = func(*valid_args, **kwargs)
            return res

        return inner

    return decorator


@clear_symbol_in_text(",")
def print_text_without_commas(text):
    print(text)


@clear_symbol_in_text(" ")
def print_text_without_spaces(text):
    print(text)


print(txt)
print_text_without_commas(txt)
print_text_without_spaces(txt)
