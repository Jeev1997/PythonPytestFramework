
import pytest

from playwright.sync_api import Page, expect

def test_frame(page:Page):
    page.goto("https://ui.vision/demo/webtest/frames/frame_1")

    frame = page.frames
    print("no of frames in page", len(frame))

    frame = page.frame_locator("//input[@name='mytext1']")
    frame.locator("//input[@name='mytext1']").fill("Hello world")
    page.wait_for_timeout(5000)