# This script reads a file named "periodic_table.txt" and creates an HTML file named "periodic_table.html" with the content of the file in a table format.

def main():
    try:
        with open("periodic_table.txt", "r") as File:
            lines = File.readlines()
            html = open("periodic_table.html", "w")
            html.write('''<!DOCTYPE html>
            <html lang="en">
            <head>
            <meta charset="UTF-8">
            <title>Periodic Table</title>
            <style>
                td{border: 1px solid black; padding:10px;}
            </style>
            </head>
            <body>''')
            html.write("<table>")
        for line in lines:
            name = line.split('=')[0]
            position = line.split('=')[1]
            properties = line.split('=')[1].split(',')
            position = properties[0]
            position = position.split(':')
            number = properties[1]
            symbol = properties[2]
            molar = properties[3]
            if position[1] == '0':
                html.write("<tr>")
                cur_position = 0
            for i in range(cur_position, int(position[1]) - 1):
                html.write(f"<td style='border: none'></td>")
            html.write(f'''<td><h4>{name}</h4>''')
            html.write("<ul>")
            html.write(f'''<li>{number}</li>''')
            html.write(f'''<li>{symbol}</li>''')
            html.write(f'''<li>{molar}</li>''')
            html.write("</ul>")
            html.write("</td>")
            if position[1] == '17':
                html.write("</tr>")
            cur_position = int(position[1])
        html.write("</table>")
        html.write("</body>")
    except FileNotFoundError:
        print("File not found")
        return

if __name__ == '__main__':
    main()