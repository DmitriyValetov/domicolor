import numpy as np
import domicolor



def test_get_palette():
    test_img = np.ones((10,100,3))
    test_img[:, :50, :] *= (255,0,0)
    test_img[:, 50:80, :] *= (0,255,0)
    test_img[:, 80:, :] *= (0,0,255)
    test_img = test_img.astype('uint8')
    colors_and_portions = domicolor.get_palette(test_img, 6)
    assert len(colors_and_portions) == 3
    
    assert colors_and_portions[0][0] == (255, 0, 0)
    assert abs(colors_and_portions[0][1]-0.5)<0.000001
    
    assert colors_and_portions[1][0] == (0, 255, 0)
    assert abs(colors_and_portions[1][1]-0.3)<0.000001

    assert colors_and_portions[2][0] == (0, 0, 255)
    assert abs(colors_and_portions[2][1]-0.2)<0.000001


