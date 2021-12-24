from argparse import ArgumentParser
import os

report_name = "report.html"
survivor_graph = "log.png"
net_extension = ".svg"

def write_header(output_file):
    html_code = f"""
    <html>
    <head>
        <style>
        table, th, td {
          border: 1px solid black;
          border-collapse: collapse;
        }
        </style>
    </head>
    <body>
        <h1>Biosim report</h1>
        <img 
            src="{survivor_graph}" 
        />
    """
    output_file.write(html_code)


def write_footer(output_file):
    output_file.write('</body></html>')

def write_video_cell(output_file,video_filename):
    html_code = f"""
        <td>
            <video class="tab" controls
            height="400"
            width="400">
                <source src="{video_filename}"/>
              </video>
        </td>
    """
    output_file.write(html_code)

def write_net_cell(output_file,net_filename):
    html_code = f"""
        <td>
            <img 
                src="{net_filename}" 
                height="400"
                width="400"
            />
        </td>
    """.replace('video_filename',net_filename)
    output_file.write(html_code)

def process_net_files(output_file,input_dir,generation_prefix):
    for filename in os.listdir(input_dir):
        if filename.endswith(net_extension) and  filename.startswith(generation_prefix):
            write_net_cell(output_file,filename)

def process_generation(output_file,input_dir,video_filename,video_extension):
    generation_prefix = video_filename.replace(video_extension,'')
    generation = generation_prefix.replace('gen-','')
    
    #output_file.write("<tr><td>")
    
    #output_file.write("</td></tr>")
    output_file.write("<tr>")
    output_file.write(f"<h2>Generation: {generation}</h2>")
    write_video_cell(output_file,video_filename)
    
    process_net_files(output_file,input_dir,generation_prefix)
    output_file.write("</tr>")


def process_generations(output_file,input_dir,video_extension):
    output_file.write("<table>")
    files = []
    for filename in os.listdir(input_dir):
        if filename.endswith(video_extension):
            files.append(filename)
    
    for filename in sorted(files):
        process_generation(output_file,input_dir,filename,video_extension)
    output_file.write("</table>")


def make_report(input_dir,video_extension):
    full_filename = input_dir + os.path.sep + report_name
    output_file = open(full_filename, "w")
    
    write_header(output_file)
    process_generations(output_file,dirname,video_extension)
    write_footer(output_file)

    output_file.close()

if __name__ == "__main__":
    parser = ArgumentParser(description="Convert a net txt file to a graph\n")
    requiredNamed = parser.add_argument_group('required arguments')
    requiredNamed.add_argument("--dir", "-d", help="Directory with net txt files", type=str,required=True,default=None)

    parser.add_argument("--videoextension", "-e", help="Extension of the video files", type=str,default=".ogv")

    args = parser.parse_args()
    video_extension =args.videoextension
    dirname =args.dir

    make_report(dirname,video_extension)
    