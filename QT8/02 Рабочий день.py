from PIL import Image, ImageDraw


def workplace(w, background='#fac372', armchair='#a9d18e',
              c_armchair='#548235', table='#963', shelf='#843cc0',
              cat='#7c7c7c', book='#2f5597'):
    im = Image.new(mode="RGB", size=(w * 24, w * 20), color=background)
    drawer = ImageDraw.Draw(im)
    # часы
    drawer.ellipse((2 * w, 3 * w, 8 * w, 9 * w), fill='#FFFFFF', outline=shelf, width=round(w * 0.2))
    drawer.line((5 * w, 3 * w, 5 * w, 6 * w), fill=shelf, width=round(w * 0.2))
    drawer.line((5 * w, 6 * w, 7 * w, 6 * w), fill=shelf, width=round(w * 0.2))
    # кресло
    drawer.ellipse((2 * w, 12 * w, 8 * w, 17 * w), fill=armchair,
                   outline=c_armchair, width=round(w * 0.2))
    drawer.ellipse((1 * w, 16 * w, 9 * w, 18 * w), fill=armchair,
                   outline=c_armchair, width=round(w * 0.2))
    drawer.ellipse((1 * w, 14 * w, 3 * w, 20 * w), fill=armchair,
                   outline=c_armchair, width=round(w * 0.2))
    drawer.ellipse((7 * w, 14 * w, 9 * w, 20 * w), fill=armchair,
                   outline=c_armchair, width=round(w * 0.2))
    # книги
    drawer.rectangle((21 * w, 1 * w, 22 * w, 4 * w), fill='#ff0')
    drawer.rectangle((12 * w, 5 * w, 13 * w, 9 * w), fill='#2f5597')
    drawer.rectangle((13 * w, 6 * w, 14 * w, 9 * w), fill='#548235')
    drawer.rectangle((20 * w, 6 * w, 21 * w, 9 * w), fill='#ffc000')
    drawer.rectangle((11 * w, 10 * w, 12 * w, 14 * w), fill='#cf417a')
    drawer.rectangle((12 * w, 11 * w, 13 * w, 14 * w), fill='#e67110')
    # полка
    drawer.line((10 * w, 0 * w, 10 * w, 20 * w), fill=shelf, width=round(w * 0.5))
    drawer.line((23 * w, 0 * w, 23 * w, 20 * w), fill=shelf, width=round(w * 0.5))
    drawer.line((10 * w, 4 * w, 23 * w, 4 * w), fill=shelf, width=round(w * 0.5))
    drawer.line((10 * w, 9 * w, 23 * w, 9 * w), fill=shelf, width=round(w * 0.5))
    drawer.line((10 * w, 14 * w, 23 * w, 14 * w), fill=shelf, width=round(w * 0.5))
    # кот
    drawer.ellipse((17 * w, 11 * w, 19 * w, 13 * w), fill=cat)
    drawer.ellipse((18 * w, 12 * w, 22 * w, 14 * w), fill=cat)
    drawer.ellipse((round(21.5 * w), 13 * w, round(22.5 * w), 17 * w), fill=cat)
    drawer.polygon((17 * w, 11 * w, 17 * w, 12 * w, 18 * w, 12 * w), fill=cat)
    drawer.polygon((19 * w, 11 * w, 19 * w, 12 * w, 18 * w, 12 * w), fill=cat)
    # стол
    drawer.polygon((11 * w, 16 * w, 17 * w, 16 * w, 17 * w, 17 * w, 16 * w, 17 * w,
                    16 * w, 20 * w, 15 * w, 20 * w, 15 * w, 17 * w, 13 * w, 17 * w,
                    13 * w, 20 * w, 12 * w, 20 * w, 12 * w, 17 * w, 11 * w, 17 * w),
                   fill=table)
    drawer.rectangle((12 * w, 15 * w, 16 * w, 16 * w), fill=book)
    im.save('workplace.png')


params = {'armchair': '#66c450', 'book': '#00c', 'shelf': '#6c3524'}
workplace(20, **params)
