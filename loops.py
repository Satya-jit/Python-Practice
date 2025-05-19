list_of_cloud = ['AWS', 'Azure', 'GCP', 'IBM Cloud', 'Oracle Cloud']

cloud = 'AWS'

print(list_of_cloud)


list_of_cloud.append('Alibaba Cloud')


list_of_cloud.append('Digital Ocean')
list_of_cloud.append('Linode')

print(list_of_cloud)

list_of_cloud.insert(0, 'Hello world')

print(list_of_cloud)

for cloud in list_of_cloud:

    print(cloud)

    for i in range(1, 10):
        print(i)