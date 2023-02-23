from time import perf_counter

from copylot.hardware.cameras.avt.camera import AVTCamera


def main():
    camera = AVTCamera()

    # acquire single frame
    start_time = perf_counter()
    AVTCamera().acquire_single_frame()
    stop_time = perf_counter()
    print(stop_time - start_time)

    # get exposure bounds for all available cameras
    print(camera.exposure_bounds)

    # check temperature
    print(camera.temperature)


if __name__ == '__main__':
    main()
