# Andrew Thompson, Darren M Ashcroft, Lynn Owens, Tjeerd P Van Staa, Munir Pirmohamed, 2023.

import sys, csv, re

codes = [{"code":"66e0.00","system":"readv2"},{"code":"7P22100","system":"readv2"},{"code":"8CAv.00","system":"readv2"},{"code":"8H7p.00","system":"readv2"},{"code":"8HHe.00","system":"readv2"},{"code":"8HkG.00","system":"readv2"},{"code":"8HkJ.00","system":"readv2"},{"code":"8IAF.00","system":"readv2"},{"code":"8IAJ.00","system":"readv2"},{"code":"8IAt.00","system":"readv2"},{"code":"8IEA.00","system":"readv2"},{"code":"9NN2.00","system":"readv2"},{"code":"9k1..00","system":"readv2"},{"code":"9k11.00","system":"readv2"},{"code":"9k12.00","system":"readv2"},{"code":"9k14.00","system":"readv2"},{"code":"9k1A.00","system":"readv2"},{"code":"9k1B.00","system":"readv2"},{"code":"Z191100","system":"readv2"},{"code":"Z191211","system":"readv2"},{"code":"ZV57A00","system":"readv2"},{"code":"ZV6D600","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('psychosocial-support-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["psychosocial-support-valcohol---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["psychosocial-support-valcohol---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["psychosocial-support-valcohol---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
