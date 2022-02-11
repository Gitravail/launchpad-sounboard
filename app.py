class App:

    def __init__(self, w, h, output_device):
        """
        Init launchpad mock

        :param w: width of the launchpad grid
        :param h: height of the launchpad grid
        :param output_device: set where the sounds are going to be played

        """
        self.size = (w, h)
        self.output_device = output_device
