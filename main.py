import scrapetube, pythumb, os

# TODO: Allow user to input channel link and aut find channel ID
# TODO: Add GUI

chan = input("input the channel ID for whose thumbnails you'd like downloaded: ").strip()

def main():
    videos = scrapetube.get_channel(chan)
    id_list = []
    number = 1
    for video in videos:
        id_list.append(video['videoId'])
        
    for id in id_list:
        url = pythumb.Thumbnail(f"https://www.youtube.com/watch?v={id}")
        url.fetch()
        url.save("./thumbnails")
        print(f"thumbnail {number} downloaded")
        number += 1

def create_new_dir():
    current_directory = os.getcwd()
    final_directory = os.path.join(current_directory, r'thumbnails')
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)
    print("thumbnails directory created")

print("The program will create a new folder titled \'thumbnails\' and download the channel's thumbmnails into that folder")


start = input("Would you like to proceed? [y/n]").lower()


if start == 'y' or start == 'yes':
    print("Starting download")
    create_new_dir()
    main()

else:
    print("Aborting")