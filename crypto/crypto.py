text = "ZASKKJOMISZZUGGSYIKVODRVJUMHRRZHOFJRYOWNOURROUZVJNDGTSEVCJZVFAONKRIHAEUEGGRATKKKSKZZTZIFJVXEMATXRHUAIEUMWUKKNTHLNVYHZVOVXLOJKEUMAGZZBTHWJKUKSLXVGMXMYKUKSNKESTWFRPHRHZKZXKOLOFTTZSYJKLGEKEZHTLNVJTBYKIYHTTGKZESSTUHRHZKZXLSDLZTMSJKJZKOLNVXMVWEUOLQGBVXTGGAEJKSSYFTMCJAEGPOQHPXXODOQOGULNRZPVSZZZFOCKJYXBKKWUKHZKDZHRGJVVXBVYFTPVSZZZPWDRDGDSKKEYXTGXFZASJYKUWCSTUZAOLGCRHTLNVUMVWXJITBFUKOVSLNZYMCGKMKGOIAZZXPJGMKLCDJZKKASEGXXTWXKUKIFXRZASJZYGGVWXFOVODRPHNHHUZTMZWYJRRRAKKXRWFMKULHWSKNXCFIFSBBYZZJXODRSEAWEYVRYHZAJCXQGACJBASMZTXKAZYUNHUUEZKOVOTZBCFGTOKQMSJZTBUKZTPVAIYGGOJSPGEZGLNNHGWSVSUSJYRXXPJGMKYZWKJGMHGVJVXSVHVLHFWZYKXBWSPSTYWYRSHJWOWZASKUCJBSJYIKTZDERXXPJGMKMVWTKNBGKAIKEMAYEZMVWULZVCEKRTRCXZYKFKSTKKWSSIYCHIDJYGOSHXVLXFJKUZAOLGCRLHSTUGGRXOXNMKZGKCXVSBVNXFWZYKGWKGTGLSATNNBQZZYKBBLKIGVHAUEUYASTPOGRABZJNODRPXTHAUEGERWIZYBCFSRQBBYVIUVSKYVYHBWVIUVSKYGKKGGRUOXFHXFJNQWYRTHILIFSXWFZVTWSVHPTHCFKDULHSXDOXGLXPZHONUZJMVAYGXHPDKDPNGLGJIHFLKQJBRKOEIXHZKPITBLAJATZDEDGDSJKKXXOLVYELWUGCRRWEVFYLWTRVZASQSRQXWLKTUGCEOTGEZQODVHGKOSRXHZKPYACGZUKLSJZVXLHZKEYMOFJZTZOFJWOZVLOEMBGWGTNLCDJZKKGATUOOWVARREMJGKOHBSRTUNFKKFLTQLOFTTTLKIGEZTKTGNGWZYKVCKZFLKIFTZTZWKYLXXHGHVGMZWGJZTGZOXNTGLNVIHGLUWYMOQOEM"
text2 = "THESESITUATIONSASRECALLEDBYPLATOANDASVIVIDLYACTEDUPONBYCORTEZHAVEACOMMONANDINTERESTINGUNDERLYINGLOGICNOTICETHATTHESOLDIERSARENOTMOTIVATEDTORETREATJUSTOREVENMAINLYBYTHEIRRATIONALASSESSMENTOFTHEDANGERSOFBATTLEANDBYTHEIRSELFINTERESTRATHERTHEYDISCOVERASOUNDREASONTORUNAWAYBYREALIZINGTHATWHATITMAKESSENSEFORTHEMTODODEPENDSONWHATITWILLMAKESENSEFOROTHERSTODOANDTHATALLOFTHEOTHERSCANNOTICETHISTOOEVENAQUITEBRAVESOLDIERMAYPREFERTORUNRATHERTHANHEROICALLYBUTPOINTLESSLYDIETRYINGTOSTEMTHEONCOMINGTIDEALLBYHIMSELFTHUSWECOULDIMAGINEWITHOUTCONTRADICTIONACIRCUMSTANCEINWHICHANARMYALLOFWHOSEMEMBERSAREBRAVEFLEESATTOPSPEEDBEFORETHEENEMYMAKESAMOVEIFTHESOLDIERSREALLYAREBRAVETHENTHISSURELYISNTTHEOUTCOMEANYOFTHEMWANTEDEACHWOULDHAVEPREFERREDTHATALLSTANDANDFIGHTWHATWEHAVEHERETHENISACASEINWHICHTHEINTERACTIONOFMANYINDIVIDUALLYRATIONALDECISIONMAKINGPROCESSESONEPROCESSPERSOLDIERPRODUCESANOUTCOMEINTENDEDBYNOONEMOSTARMIESTRYTOAVOIDTHISPROBLEMJUSTASCORTEZDIDSINCETHEYCANTUSUALLYMAKERETREATPHYSICALLYIMPOSSIBLETHEYMAKEITECONOMICALLYIMPOSSIBLETHEYSHOOTDESERTERSTHENSTANDINGANDFIGHTINGISEACHSOLDIERSINDIVIDUALLYRATIONALCOURSEOFACTIONAFTERALLBECAUSETHECOSTOFRUNNINGISSURETOBEATLEASTASHIGHASTHECOSTOFSTAYING"

def caesar(string, number):
    while number < 0:
        number += 26
    while number > 26:
        number -= 26
    splitted_list = [char for char in string.lower()]
    empty_list = []
    for letter in splitted_list:
        if ord(letter) + number > 122:
            empty_list.append(chr(ord(letter) + number - 26))
        else:
            empty_list.append(chr(ord(letter) + number))
    return "".join(empty_list).upper()
#  a = 97, b = 98 ... x = 120, y = 121, z = 122


def frequency(string):
    dictionary = {}
    splitted_list = [char for char in string.lower()]
    for number in range(97, 123):
        dictionary[chr(number).upper()] = splitted_list.count(chr(number)) / len(string) * 100
    # for number in range(97, 123):                 For checking if percentages add up to 100%
    #     sum += dictionary[chr(number).upper()]    They add up to 99,999999999999999%
    return dictionary

def index_of_coincidence(string):
    sum = 0
    splitted_list = [character for character in string.lower()]
    for ascii_code in range(97, 123): # 97 is ascii code for 'a' and 122 (123-1) is ascii code for 'z'
        sum += splitted_list.count(chr(ascii_code)) * (splitted_list.count(chr(ascii_code)) - 1)
    return sum / (len(splitted_list) * (len(splitted_list) - 1))

#print(index_of_coincidence(text))
max_length = 6

def find_key_length(string, possible_length):
    lists_of_letters = {} # Here are stored lists with letters in them. These lists will be turned into substrings.
    list = [] # List for substrings.
    splitted_list = [char for char in string.lower()]  # Splits ciphertext into letters.
    for i in range(possible_length): # Makes as many empty lists for making substrings as long is the possible key.
        lists_of_letters[i] = []     # e.g. key with length of 2 letters means 2 substrings -> 2 empty lists
    for index in range(len(splitted_list)):
        lists_of_letters[index%possible_length].append(splitted_list[index]) # Sorts letters evenly into lists.
    for list_index in range(len(lists_of_letters)):
        list.append(''.join(lists_of_letters[list_index])) # Joins letters in the lists into substrings that go to list.
    for substring in list:
        #print(index_of_coincidence(substring)) # Calculates Index of Coincidence for every substring.
        print(frequency(substring)) # Finds relative frequencies of letters.

def encrypt_decrypt(string, key):
    lists_of_letters = {} # Here are stored lists with letters in them. These lists will be turned into substrings.
    output_list = []
    splitted_list = [char for char in string.lower()]  # Splits text into letters.
    for i in range(len(key)): # Makes as many empty lists for making substrings as long is the possible key.
        lists_of_letters[i] = []     # e.g. key with length of 2 letters means 2 substrings -> 2 empty lists
    for index in range(len(splitted_list)): # This for loop sorts shifted letters (with caesar) into separate lists.
                                            # 97 is the ASCII code of "a". To make the shift in range of 0-25
                                            # it substracts 97 from it
        lists_of_letters[index%len(key)].append(caesar(splitted_list[index], ord(key.lower()[index%len(key)]) - 97))
    length_of_substring = len(lists_of_letters[0]) # Defines maximum length of one list of letters.
    for list_index in range(len(lists_of_letters)):
        if (len(lists_of_letters[list_index]) < length_of_substring): # Checks the length of list of letters.
            lists_of_letters[list_index].append(" ")  # If the lists are not even length then adds a space in it
                                                      # to make it even.
    for i in range(len(lists_of_letters[0])):
        for size in range(len(lists_of_letters)):
            output_list.append(lists_of_letters[size][i]) # Adds letters in lists into one list.
    print(''.join(output_list)) # Joins the letters in list.


encrypt_decrypt(text2,"GTOSGR")



