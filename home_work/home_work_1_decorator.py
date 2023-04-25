txt = "Значимость этих проблем настолько очевидна, что новая модель организационной деятельности влечет за собой " \
      "процесс внедрения и модернизации позиций, занимаемых участниками в отношении поставленных задач. " \
      "Практический опыт показывает, что постоянное информационно-техническое обеспечение нашей деятельности " \
      "способствует подготовке и реализации позиций, занимаемых участниками в отношении поставленных задач. " \
      "Задача организации, в особенности же дальнейшее..."


def clear_symbol_in_text(symbol):
    def decorator(func):
        symbols = []

        def inner(*args, **kwargs):
            valid_args = []
            for arg in args:
                valid_args.append(str(arg).replace(symbol, ""))
                symbols.append(symbol)
            res = func(*valid_args, **kwargs)
            # print(symbols)
            print(f"Из текста убран символ: `{symbol}`")
            return res

        return inner

    return decorator


@clear_symbol_in_text(",")
@clear_symbol_in_text(" ")
def print_text_without_symbols(text):
    print(text)


print(txt)
print_text_without_symbols(txt)
