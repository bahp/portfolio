#!/usr/bin/env python3
import asyncio
from pyppeteer import launch

async def generate_pdf(sourcepath, outfile):
    """Works for pdf files

    Parameters
    ----------
    sourcepath: string
        The source of the html file.
    outfile: string
        The path to save the image.

    """
    browser = await launch()
    page = await browser.newPage()
    await page.goto(sourcepath, {'waitUntil': 'networkidle2'})
    await page.pdf({
      'path': outfile,
      'format': 'A3',
      'printBackground': True,
      'margin': {
        'top': 0,
        'bottom': 0,
        'left': 0,
        'right': 0
      }
    })
    await browser.close()


async def generate_png(sourcepath, outfile):
    """Works or png and jpg

    Parameters
    ----------
    sourcepath: string
        The source of the html file.
    outfile: string
        The path to save the image.

    """
    browser = await launch({
        #'args': ['--window-size=500,200']
    })
    page = await browser.newPage()
    await page.goto(sourcepath)
    await page.screenshot({'path': outfile, 'fullPage': False})
    await browser.close()





if __name__ == '__main__':

    # Generic
    import yaml

    # Specific
    from pathlib import Path
    from yaml.loader import SafeLoader

    # Constants
    OUTPATH = 'docs/static/imgs/'

    # Load configuration
    CONFIG = None
    with open('config.yaml') as f:
        CONFIG = yaml.load(f, Loader=SafeLoader)

    # Total number of projects
    PROJECTS = CONFIG['portfolio']['projects']

    # Create items information
    for i, e in enumerate(PROJECTS):
        print("{i}/{tot}. Creating thumbnail... {name}".format(
              i=i+1, tot=len(PROJECTS), name=e['name']))
        try:
            sourcepath = e.get('url')
            outputpath = '%s/thumbnail-%s.jpg' % (OUTPATH, e.get('name'))
            asyncio \
                .get_event_loop() \
                .run_until_complete( \
                    generate_png(sourcepath, outputpath))
        except Exception as e:
            print(e)