# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 00:09:38 2021
@author: Richard Paglia

"""

totalFamily = {}

allFamily = [{'Name': 'Richie', 'Birthdate': '01/01/1972','Color': 'Dark Grey', 'Artist': 'Def Leppard'},
{'Name': 'Eric Cartman', 'Birthdate': '07/01/1997','Color': 'Red', 'Artist': 'Faith+1'},
{'Name': 'Stan Marsh', 'Birthdate': '10/19/1997','Color': 'Blue', 'Artist': 'Moop'},
{'Name': 'Kyle Broflovski', 'Birthdate': '05/26/1997','Color': 'Green', 'Artist': 'Fingerb*ng'},
{'Name': 'Kenny McCormick', 'Birthdate': '03/22/1997','Color': 'Orange', 'Artist': 'Moop'}]


def memberDeletion():
    #Remove family member
        memberToDelete = input('Family member to remove: ')
        for element in allFamily:
            if memberToDelete in element['Name']:
                result = next(item for item in allFamily if item['Name'] == memberToDelete)
                allFamily.remove(result)
                print(f'\033[0;43;mDeleting the family member "{memberToDelete}" from the family list!!\n\033[0;0;m')
                return
        
        print(f'\033[0;31;m{memberToDelete} does not exists in the family list.\033[0;0;m')

def memberAddition():
    #Need to add error correction to this block!!
    memberName = input('Enter name of the family member: ')
    memberBirthdate = input('Enter birthdate of the family member mm/dd/yyyy: ')
    memberColor = input('Enter the family member\'s favorite color: ')
    memberArtist = input('Enter the family member\'s favorite artist: ')

    memberInfo={'Name':memberName,'Birthdate':memberBirthdate,'Color':memberColor,'Artist':memberArtist}
    totalFamily = memberInfo
    allFamily.append(totalFamily)
    return allFamily 
 
def menu():
    while True:
        print ("\n\n\nFamily Dictionary Menu")
        print ("\033[0;36;m----------------------\033[0;0;m")
        print ("1) Display Family Dictionary")
        print ("2) Add family member to Dictionary")
        print ("3) Remove family member from Dictionary")    
        print ("Q) Exit\n")
        choice = input('Enter your choice: ').lower()
        
        if choice == '1':
            if allFamily:
                allFamilySorted = sorted(allFamily , key = lambda i: (i['Name'], i['Birthdate']))
                print('\n\nCurrent Family Members in Dictionary')
                print("\033[0;36;m------------------------------\033[0;0;m")
                print(*allFamilySorted, sep = '\n' )
            else:
                print("\n\033[0;31;mThe family dictionary is currently empty...\033[0;0;m")
                input('Press Enter to return to menu...')
        elif choice == '2':
            memberAddition()
        elif choice == '3':
            memberDeletion()
        elif choice == 'q':
            return
        else:
            print(f'\033[0;31;mNot a correct choice: <{choice}>,try again\033[0;0;m')
 
if __name__ == '__main__':
    menu()    
    


