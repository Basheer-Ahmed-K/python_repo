import numpy
import logging


def FloorCeilRint(array):
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    numpy.set_printoptions(legacy='1.13')
    # logging.info("%s %s %s \n", numpy.floor(array), numpy.ceil(array), numpy.rint(array))
    ans = numpy.array([numpy.floor(array), numpy.ceil(array), numpy.rint(array)])
    # logging.info(ans)
    print(numpy.array(ans))
    # return numpy.floor(array), numpy.ceil(array), numpy.rint(array)
    return numpy.array(ans)
