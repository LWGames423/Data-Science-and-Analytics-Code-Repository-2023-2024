import re

def replace_multiple_spaces_with_comma(input_file, output_file):
  """Replaces strings of more than 2 spaces with a comma in a file.

  Args:
    input_file: The path to the input file.
    output_file: The path to the output file.
  """

  with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
    for line in f_in:
      line = re.sub(r'\s{2,}', ',', line)
      f_out.write(line)


def remove_leading_commas(input_file, output_file):
  """Removes all leading commas from each line in a file.

  Args:
    input_file: The path to the input file.
    output_file: The path to the output file.
  """

  with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
    for line in f_in:
      line = re.sub(r'^,+', '', line)
      f_out.write(line)

if __name__ == '__main__':
    input_file = 'data.txt'
    output_file = 'output.txt'
    output_file2 = "outpu2.txt"
    replace_multiple_spaces_with_comma(input_file, output_file)
    remove_leading_commas(output_file, output_file2)
