'''
 A simple program counting the number of frames vector actually streams to the computer by counting the number
 of different images streamed in ten seconds then outputting the average fps.
 Author: Tony Pan
 Date: 01-21-2019
'''


import datetime
import anki_vector


def main():
    with anki_vector.Robot(enable_camera_feed=True) as robot:           # init vector robot object with camera enabled
        start_time = datetime.datetime.now()                            # starting system time
        count = 0                                                       # number of frames
        raw_img = robot.camera.latest_image                             # get the latest frame
        prev_img = raw_img.resize((32, 32))                             # resize the img onbard before streaming
        prev_img_time_stamp = robot.last_image_time_stamp               # get the time stamp of the latest image in ms
        while (datetime.datetime.now() - start_time).seconds < 10:      # let the program run for 10 seconds
            raw_img = robot.camera.latest_image                         # get the latest frame
            current_img = raw_img.resize((32, 32))                      # resize the img onboard before streaming
            if current_img != prev_img:                             # if the latest frame is different from the previous
                count = count + 1                                       # increment count
                current_img_time_stamp = robot.last_image_time_stamp    # get the time stamp from the latest frame in ms
                print((current_img_time_stamp - prev_img_time_stamp) / 100)  # print the elapse time in sec
                prev_img_time_stamp = current_img_time_stamp            # update the previous time stamp
                prev_img = current_img                                  # update the previous image
        print(count / 10)                                               # after ten seconds, print the average fps


if __name__ == "__main__":
    main()
