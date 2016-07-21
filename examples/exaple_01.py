
import numpy
import itf_barcode_reader as barcode_reader

# Array of test barcode
test_barcode_array = numpy.array(
    [0.17647059,  0.16862746,  0.16078432,  0.16078432,  0.15686275,
     0.16078432,  0.16078432,  0.15686275,  0.14901961,  0.14509805,
     0.14117648,  0.13725491,  0.13725491,  0.13725491,  0.13333334,
     0.12941177,  0.1254902,  0.12941177,  0.13333334,  0.15294118,
     0.29019609,  0.43137255,  0.47450981,  0.47843137,  0.35294119,
     0.20784314,  0.28235295,  0.42745098,  0.49019608,  0.50196081,
     0.38431373,  0.21176471,  0.25882354,  0.3764706,  0.47058824,
     0.50980395,  0.42352942,  0.27450982,  0.3019608,  0.41960785,
     0.48627451,  0.51372552,  0.42745098,  0.28235295,  0.26274511,
     0.33333334,  0.45882353,  0.53333336,  0.5411765,  0.5529412,
     0.54901963,  0.5411765,  0.52156866,  0.47843137,  0.29411766,
     0.16078432,  0.13333334,  0.11764706,  0.11764706,  0.1254902,
     0.21568628,  0.37254903,  0.45490196,  0.50980395,  0.52156866,
     0.52941179,  0.52941179,  0.52549022,  0.45882353,  0.33725491,
     0.21176471,  0.14117648,  0.13725491,  0.13333334,  0.13725491,
     0.15294118,  0.29019609,  0.45882353,  0.48235294,  0.45882353,
     0.28235295,  0.17647059,  0.29411766,  0.4627451,  0.48235294,
     0.47843137,  0.32156864,  0.1882353,  0.29411766,  0.4627451,
     0.49411765,  0.48627451,  0.33725491,  0.19215687,  0.28627452,
     0.44705883,  0.49411765,  0.52156866,  0.52941179,  0.5411765,
     0.53725493,  0.52941179,  0.4509804,  0.3137255,  0.18431373,
     0.10196079,  0.08627451,  0.08235294,  0.09803922,  0.14901961,
     0.30588236,  0.47450981,  0.51372552,  0.53725493,  0.53333336,
     0.53333336,  0.52156866,  0.50196081,  0.38039216,  0.19215687,
     0.12941177,  0.09411765,  0.09019608,  0.09803922,  0.15686275,
     0.28235295,  0.41568628,  0.50980395,  0.44313726,  0.3137255,
     0.23921569,  0.27058825,  0.40392157,  0.51372552,  0.52549022,
     0.52941179,  0.52941179,  0.52941179,  0.51372552,  0.47058824,
     0.29019609,  0.13333334,  0.10588235,  0.09803922,  0.10196079,
     0.12156863,  0.21568628,  0.36078432,  0.4627451,  0.52941179,
     0.53333336,  0.53725493,  0.53333336,  0.52549022,  0.49411765,
     0.41960785,  0.25882354,  0.19607843,  0.35686275,  0.48627451,
     0.47843137,  0.41960785,  0.25882354,  0.21176471,  0.36470589,
     0.48627451,  0.49803922,  0.45882353,  0.28235295,  0.19607843,
     0.35686275,  0.48627451,  0.49411765,  0.4627451,  0.27450982,
     0.1254902,  0.09803922,  0.08235294,  0.08627451,  0.09803922,
     0.19607843,  0.34509805,  0.4509804,  0.52156866,  0.52549022,
     0.53725493,  0.53333336,  0.52941179,  0.47843137,  0.37254903,
     0.25490198,  0.21960784,  0.38431373,  0.49019608,  0.46666667,
     0.38039216,  0.21960784,  0.11372549,  0.10196079,  0.09803922,
     0.09803922,  0.10196079,  0.10196079,  0.09411765,  0.09411765,
     0.09411765,  0.09411765,  0.09411765,  0.09019608,  0.09411765])


if __name__ == '__main__':
    """Use barcode reader to parse array for ITF barcode value. Changed
       length_threshold to 1 for better parsing of an array with smaller
       barcode lines"""
    barcode = barcode_reader.read_barcode(test_barcode_array,
                                          length_threshold=1)
    print "Barcode is: {}".format(barcode)
