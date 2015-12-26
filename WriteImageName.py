#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      MITESH
#
# Created:     25-12-2015
# Copyright:   (c) MITESH 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os
import PIL
import PIL.Image
import PIL.ImageDraw

def getParticipants():
    return {
    1 : 'Abhay Jayeshkumar Shukla',
    2 : 'ABHISHEK R. SHIRSAT',
    3 : 'Aditiba Rajendrasinh Raol',
    4 : 'Akshay Harith',
    5 : 'ANANT SHAHANE',
    6 : 'Anmol Shah',
    7 : 'Ashok M. Chaudhary',
    8 : 'BALAJI LOGANATHAN',
    9 : 'Bedanta B. Deka',
    10 : 'BINDU C. SHAH',
    11 : 'C. R. Sathyanarayana',
    12 : 'Chaudhari Mukesh Kashirambhai',
    13 : 'Chaudhari Shailja Mukeshbhai',
    14 : 'Chetanbhai M. Vala',
    15 : 'Dhairya Dixit',
    16 : 'Dimple J. Raval',
    17 : 'DR. AMIT M. PATEL',
    18 : 'DR. DHARMESH B. PATEL',
    19 : 'Dr. Muralidhar G',
    20 : 'Dr. N. M. Shaikh',
    21 : 'Firoz Khan Pathan',
    22 : 'H. Satish',
    23 : 'Harish Manilal Lakhani',
    24 : 'HARSHAD S. TRIMUKHE',
    25 : 'HITESH SURATI',
    26 : 'HITESH TOPIWALA',
    27 : 'Jagat Harishbhai Raval',
    28 : 'Jiten Shaileshkumar Shah',
    29 : 'Kallol Mukherjee',
    30 : 'KAMLESH T. THAKUR',
    31 : 'Mahesh Laxminarayan Kedarpawar',
    32 : 'Manish Trivedi',
    33 : 'Manoj Kajriwal',
    34 : 'MURANI AHMAD',
    35 : 'Naman Ketan Doshi',
    36 : 'Narendra P. Modha',
    37 : 'Nilesh Bhadla',
    38 : 'Nitin S. Jain',
    39 : 'Noormohammad H. Rathod',
    40 : 'Osmangani Khatri',
    41 : 'PARESH PARADKAR',
    42 : 'Parth Pradeepbhai Chauhan',
    43 : 'Payal M. Patel',
    44 : 'Prathamesh Vinod Ghadekar',
    45 : 'Pratik Uday Pradhan',
    46 : 'Praveen Siddannavar',
    47 : 'PROF. ANAND BORA',
    48 : 'PRUTHVI D. THAKOR',
    49 : 'RADHIKA D. JADEJA',
    50 : 'Rathod Jaidevsinh Gagubha',
    51 : 'Rathod Jaypalsinh Gagubha',
    52 : 'Ravalnath Balkrishna Joshi',
    53 : 'Ripan Biswas',
    54 : 'SAGAR P. KANSAGRA',
    55 : 'SHIVANI D. JADEJA',
    56 : 'SOMIL K. MAKADIA',
    57 : 'SUMAN DEY',
    58 : 'Suyash Rajesh Kadam',
    59 : 'Umesh P. Khetani',
    60 : 'Vargiya Dhaval C',
    61 : 'VIDYA V. KULKARNI',
    62 : 'Vikrantsinh Narendrasinh Zala',
    63 : 'Vinayak T. Parmar'
}

def getAnimalNames():
    return {
'S1.1.jpg' : 'abc',
'S1.3.jpg' : 'def',
'S14.6.jpg' : 'ghi',
'S17.2.jpg' : 'jkl',
'S2.1.jpg' : 'mno',
'S2.2.jpg' : 'pqr',
'S2.6.jpg' : 'stu',
'S3.1.jpg' : 'vwx',
'S3.3.jpg' : 'yza',
'S4.1.jpg' : 'bcd',
'S4.2.jpg' : 'efg',
'S4.3.jpg' : 'hij',
'S5.1.jpg' : 'klm',
'S5.4.jpg' : 'nop',
'S5.5.jpg' : 'qrs',
'S63.5.jpg' : 'tuv'}

def process():
    image_source_path = 'D:\\mitesh\\Pics\\t\\'
    image_target_path =  'D:\\mitesh\\Pics\\t\\new\\'
    participants = getParticipants()
    animals = getAnimalNames()

    i = 1
    # Get all image files
    image_files = [f for f in os.listdir(image_source_path) if os.path.splitext(f)[1] == '.jpg' ]
    for fn in image_files:
        fp = image_source_path + fn
        img = PIL.Image.open(fp)
        draw = PIL.ImageDraw.Draw(img)

        if img.width > img.height:
            # Landscape

            x = img.width / 2
            y = img.height - 20
        else:
            # Portrait

            x = img.height / 2
            y = img.width - 20

        if not fn in animals:
            print('Problem with file: {0}'.format(fn))
            continue

        pcode = int(fn[1:fn.find('.')])    # Participant Code from file name
        if not pcode in participants:
            print('Problem with participant pcode {0}. File Name: {1}'.format(pcode, fn))
            continue

        text = '{0} - {1}'.format(str.upper(participants[pcode]), animals[fn])

        draw.text((x, y), text)
        img.save(image_target_path + fn)
        i = i + 1

        print('File Name: {0} - {1} X {2}'.format(fn, img.width, img.height))


def main():
    process()

if __name__ == '__main__':
    main()
