import urllib3, argparse, dns.resolver

http = urllib3.PoolManager()


def dnschecker(ipc):
    myResolver = dns.resolver.Resolver()
    myResolver.lifetime = 4
    myResolver.nameservers = [ipc]
    try:
        myAnswers = myResolver.query("google.com", "A")
        print("%s is recursive" % (ipc))
    except:
        pass


if __name__ == "__main__":
    iplists = []
    print("DNS Recurssion Checker - Aakar Periwal")
    parser = argparse.ArgumentParser(description='DNS Recurssion Checked - Akar Periwal')
    parser.add_argument('-i', '--ip', help='IP address to check')
    parser.add_argument('-f', '--file', help='IP address to check')
    args = parser.parse_args()
    if args is not None and args.ip is not None and len(args.ip) > 0:
        badip = args.ip
        iplists.append(badip)
    else:
        if args is not None and args.file is not None and len(args.file) > 0:
            for i in open(args.file):
                iplists.append(i.rstrip())
        else:
            my_ip = http.request('GET', 'http://icanhazip.com').data.rstrip().decode("utf-8")
            print('Your public IP address is %s\n' % (my_ip))
            # Get IP To Check
            resp = input('Would you like to check {0} ? (Y/N):'.format(my_ip))
            if resp.lower() in ["yes", "y"]:
                badip = my_ip
            else:
                badip = input("\nWhat IP would you like to check?: ")
                if badip is None or badip == "":
                    sys.exit("No IP address to check.")
            iplists.append(badip)
    for i in iplists:
        dnschecker(i)
