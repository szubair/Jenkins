#!/usr/bin/python
##script help you create jsfile from env varibales.

ENVFILE='./app_envs.txt'
MODIFILE='./env-config.js'
LOG='/tmp/env-vars.log'

def create_mydict():
    my_env = {}
    with open(ENVFILE) as f:
        lines = [line.rstrip() for line in f]
    for each_line in lines:
        line_str = str(each_line)
        key = line_str.split('=')[0]
        value = line_str.split('=')[1]
        if key not in my_env:
            my_env[key] = value
        else:
            print('Found duplicate entry on key:%s and its value is:%s' % (key, value))
    return my_env

def create_jsfile():
    env_vars_dict = create_mydict()
    rows = len(env_vars_dict)
    count = 1
    f = open(MODIFILE, "w")
    f.write("window._env_ = {\n")
    #for key, value in react_env.items():
    #    print >> f, key + ': "' + value + '",'
    for key in sorted(env_vars_dict.keys()):
        if count == rows:
            print >> f, key + ': "' + env_vars_dict[key] + '"'
        else:
            print >> f, key + ': "' + env_vars_dict[key] + '",'
        count += 1
    f.write("}\n")
    f.close()

#print(create_envdict())
create_jsfile()
