with open('experimental.brute') as final:
    with open('russian_trans_firstnames.txt') as file_firstnames:
        with open('russian_trans_surnames.txt') as file_surnames:
            for i in file_surnames:
                final.write(i)