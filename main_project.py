DATA_BASE = {}


class MailClient:
    def __init__(self, server, user):
        self.server = server
        self.user = user

        if server not in DATA_BASE:
            DATA_BASE[server] = {}
        DATA_BASE[server][user] = []

    def get_server(self):
        return self.server

    def get_username(self):
        return self.user

    def receive_mail(self):
        result = DATA_BASE[self.server][self.user].copy()
        if not result:
            return '● Почта пока пуста :/'
        DATA_BASE[self.server][self.user].clear()
        return result

    def send_mail(self, server1, user1, message):
        DATA_BASE[server1][user1].append(f'● Новое сообщение  ---  {message}')


def main():
    while True:
        print('------------------------------------------')
        print('Список серверов:')
        print('Список серверов пуст /:') if not DATA_BASE else print('\n'.join(DATA_BASE.keys()))
        print('------------------------------------------')
        """Подсказки"""
        print('Команды:')
        print('    exit                                       -- выход')
        print('    createServer <server>                      -- создать сервер <server>')
        print('    transition <server>                        -- перейти на сервер <server>')
        print()
        command = input('Команда: ')
        if command == 'exit':
            break
        elif command.split()[0] == "createServer":
            DATA_BASE[command.split()[-1]] = {}
        elif command.split()[0] == "transition":
            server = command.split()[-1]
            if server not in DATA_BASE:
                print(f'Сервера {server} не сущетсует...')
                continue
            while True:
                print('------------------------------------------')
                print('Список участников сервера:')
                print('Список участников пуст /:') if not DATA_BASE[server] else print('\n'.join(DATA_BASE[server]))
                print('------------------------------------------')
                """Подсказки"""
                print('Команды:')
                print('    exit                                       -- выход')
                print('    send_message <server> <user> <message>     -- написать <message>')
                print('                                                       на <server> пользователю')
                print('                                                       <user>')
                print('    receive_mail <server> <user>               -- посмотреть сообщения')
                print('                                                  пользователя <user> на <server>')
                print('    createUser <server> <user>                 -- создать пользователя <user>')
                print('                                                  на сервере <server>')
                print('    transition <server>                        -- перейти на сервер <server>')
                print()
                server_command = input('Команда: ')
                if server_command == 'exit':
                    break
                elif server_command.split()[0] == "createUser":
                    user = MailClient(server, server_command.split()[-1])
                elif server_command.split()[0] == "send_message":
                    server_for_post = server_command.split()[1]
                    user1 = server_command.split()[2]
                    message = ' '.join(server_command.split()[3:])
                    if server_for_post not in DATA_BASE:
                        print(f'Сервера {server_for_post} не сущетсует...')
                        break
                    if user1 not in DATA_BASE[server_for_post]:
                        print(f'Пользователя {user1} не сущетсует...')
                        break
                    user.send_mail(server_for_post, user1, message)
                elif server_command.split()[0] == "receive_mail":
                    server_for_receive = server_command.split()[1]
                    username = server_command.split()[2]
                    if server_for_receive not in DATA_BASE:
                        print(f'Сервера {server_for_receive} не сущетсует...')
                        break
                    if username not in DATA_BASE[server_for_receive]:
                        print(f'Пользователя {username} не сущетсует...')
                        break
                    while True:
                        print('------------------------------------------')
                        if DATA_BASE[server_for_receive][username]:
                            print('\n'.join(DATA_BASE[server_for_receive][username]))
                        else:
                            print('● Почта пока пуста :/')
                        print('------------------------------------------')
                        """Подсказки"""
                        print('Команды:')
                        print('    exit               -- выход')
                        commands = input('Команда: ')
                        if commands == "exit":
                            break
                        else:
                            print('Неверная команда')
                        print()
                else:
                    print('Неверная команда')
                print()
                print()
        else:
            print('Неверная команда')
        print()
        print()


if __name__ == '__main__':
    main()
