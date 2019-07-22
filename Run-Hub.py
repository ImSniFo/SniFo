#By Snifo (Sofiene Hichri)
import socket
import subprocess
import time
def Hub():

    while True:
# -----------------------------------------+ Server configuratio +-----------------------------------------
        jar_name = 'Hub.jar'
        memory_by_gb = '1'
        auto_restart = 'false'
        allow_nether = 'False'
        announce_player_achievements = 'Fasle'
        enable_command_block = 'False'
        max_players = '100'
        server_port = '26456'
        server_ip = socket.gethostbyname(socket.gethostname())
        view_distance = '10'
        online_mode = 'true'
        motd = "\u00A7eHub \u00A77Server \u00A7cTunisian\u00A76Mc\u00A77 | \u00A77Connecting only with the \u00A7cBungeecord \u00A77Ip: TunisianMc.net"
# ---------------------------------------------------------------------------------------------------------
# You don't have permission to change anything

        Config = str("#Minecraft server properties\n #Mon Jul 22     19:36:43 WAT 2019\n spawn-protection=0\n "
                     "generator-settings=\n force-gamemode=false\n allow-nether={}\n gamemode=0\n enable-query=false\n"
                     " player-idle-timeout=0\n difficulty=1\n spawn-monsters=true\n op-permission-level=4\n"
                     " resource-pack-hash=\n announce-player-achievements={}\n pvp=true\n snooper-enabled=true\n"
                     " level-type=DEFAULT\n hardcore=false\n enable-command-block={}\n max-players={}\n"
                     " network-compression-threshold=256\n max-world-size=29999984\n server-port={}\n"
                     " debug=false\n server-ip={}\n spawn-npcs=true\n allow-flight=false\n level-name=world\n"
                     " view-distance={}\n resource-pack=\n spawn-animals=true\n white-list=false\n"
                     " generate-structures=true\n online-mode={}\n max-build-height=256\n level-seed=\n"
                     " motd={}\n enable-rcon=false").format(allow_nether, announce_player_achievements,
                                                            enable_command_block, max_players, server_port, server_ip,
                                                            view_distance, online_mode, motd)
        with open("server.properties", "w+") as f:
            f.write(Config)
        echo = subprocess.call("@echo off", shell=True)
        run_config = "java -Xmx{}G -jar {}".format(memory_by_gb, jar_name)
        run = subprocess.call(run_config, shell=True)


        def stop_server():
            print('Server closed')

        def restart_server():
            print("SERVER STOP")
            print("Do you want to restart the server!")
            print("Yes = |1| |  No = |2|")
            Chose = input('')
            if Chose == '1':
                print('Restarting!')
                Hub()
            elif Chose == '2':
                stop_server()
            else:
                restart_server()

        if auto_restart.lower() == "true":
            print("Auto Restarting!!")
            Hub()
        elif auto_restart.lower() == "false":
            restart_server()
            break
        else:
            print('Please Check The auto-restart True or False!!')
            break

        break

if __name__ == "__main__":
    Hub()