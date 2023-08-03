class utilShower:
    def camChecker(img):
        if img is not None:
            return "Color Camera can see :)"
        else:
            return "No Image"

    def lidarChecker(scan):
        if scan is not None:
            return "LIDAR can see :)"
        else:
            return "No LIDAR Scan"
            
