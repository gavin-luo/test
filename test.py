
import json
import os, sys
# import ffmpeg
import re


def text_fmt(src_text_file="", dest_text_file=""):

    with open(src_text_file, "r", encoding="utf-8") as f:
        lines_list = f.read().split("\n")

    ps1 = re.compile("^PS")
    ps2 = re.compile("^Ps")
    ps3 = re.compile("^ps")
    ps4 = re.compile("^xxx")
    ps5 = re.compile("^———")
    ps6 = re.compile("^xxx")
    # new_lines = []
    i = 0
    i_p = 0
    i_d = 0
    with open(dest_text_file, "w", encoding="utf-8", newline="") as f:
        for line in lines_list:
            line = line.strip()   # 去掉头每行尾空格
            line = " ".join(line.split())  # 去掉每行中间的连续空白
            # if "ps" in line or "ps：" in line or "PS：" in line or "PS:" in line or "Ps：" in line or "Ps:" in line:
            #    line = ""
            #    i_p += 1
            if ps1.match(line) or ps2.match(line) or ps3.match(line) or ps4.match(line) or ps4.match(line) or ps6.match(line):
                line = ""   # 删除本行
            #    i_d += 1
            if ps5.match(line):
                
                line = "——————————————"
            if line != "\n" and line != "":   # 写入非空行
                f.writelines(line + "\n")
                i += 1
    print("\n 全文有效行共有 %s 行" % i)


def concat_video(video_list=None, dest_video=""):
    if video_list is None or len(video_list) < 1 or dest_video == "":
        status_txt = "\n\n error, 不正确的调用。 函数名：%s " % sys._getframe().f_code.co_name
        print(status_txt)
        return "error", status_txt

    video_list_file = os.path.join(os.path.dirname(dest_video), "video_list_file.txt")
    with open(video_list_file, "w", encoding="utf-8", newline="") as f:
        for line in video_list:
            if not line == "":
                f.writelines("file '" + line + "'\n")
    try:
        out, err = (
            ffmpeg
                .input(video_list_file, f='concat')
                .output(dest_video, c='copy')
                .run(quiet=False, overwrite_output=True)
        )
    except Exception as e:
        print(e)



if __name__ == '__main__':

    """
    head_file = r"F:\作品\孩子学习注意力不集中该如何解决？\video_head.mp4"
    scene_file = r"F:\作品\孩子学习注意力不集中该如何解决？\Scene_父母看手机，孩子在学习\scene_video.mp4"

    info_head = ffmpeg.probe(head_file)
    info_scene = ffmpeg.probe(scene_file)

    with open("info_video_head.json", "w", encoding="utf-8", newline="") as f:
        f.write(json.dumps(info_head, ensure_ascii=False, indent=4))

    with open("info_video_scene.json", "w", encoding="utf-8", newline="") as f:
        f.write(json.dumps(info_scene, ensure_ascii=False, indent=4))
    
    # ffmpeg -f lavfi -i anullsrc=channel_layout=stereo:sample_rate=16000 -i {tmp_video_file} -shortest -c:v copy -c:a aac {Out_video_file}

    src_file = r"F:\作品\孩子学习注意力不集中该如何解决？\combination_list.txt"
    with open(src_file, "r", encoding="utf-8") as f:
        lines_list = f.read().split("\n")

    dest_video_file = r"F:\作品\孩子学习注意力不集中该如何解决？\test.mp4"
    concat_video(lines_list, dest_video_file)
    """
    src_file = r"drgdgdtghdrg"
    dest_file = r"fthrthysrthrt"
    text_fmt(src_file, dest_file)  
    # 这是添加的测试文字啊啊
    # 再试一行

    