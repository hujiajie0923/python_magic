import json
import csv


def write_json_data(msg=None, file_name='json_file', do_read=False):
    if do_read:
        with open('{}.json'.format(file_name), 'r', encoding='utf-8') as rf:
            read_file = rf.read()
            file = json.loads(read_file)
            print('find json data:\n', file)
            return file
    else:
        with open('{}.json'.format(file_name), 'w', encoding='utf-8') as wf:
            wf.write(json.dumps(msg, ensure_ascii=False, indent=2) + '\n')


def write_csv_data(msg=None, file_name='csv_file', do_read=False):
    if do_read:
        with open('{}.csv'.format(file_name), 'r', encoding='utf-8') as rf:
            reader = csv.reader(rf)
            print('find csv data: ')
            for line in reader:
                print(line)
            return reader
    else:
        with open('{}.csv'.format(file_name), 'a', encoding='utf-8', newline='') as wf:
            write = csv.writer(wf)
            # 写入单行
            write.writerow(['Name', 'ID'])
            write.writerow(['Evan', '66'])
            # 写入多行
            write.writerows([['Name', 'ID'], ['Evan', '66']])


if __name__ == '__main__':
    msg = {'evan': 'name'}
    # write_json_data(msg=msg)
    # write_csv_data()
