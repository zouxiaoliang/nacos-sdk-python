# coding=utf8
# 2023/11/02

import nacos
import json
__author__ = "zouxiaoliang"


def _main():
    _nacos_server_list = "127.0.0.1:8848"
    _namespace = "a1f503dd-fdc2-400e-bdd8-fae1267521b4"
    _namespace = ""
    # nacos.NacosClient.set_debugging()

    nacos_client = nacos.NacosClient(
        _nacos_server_list,
        namespace=_namespace,
        username="nacos",
        password="nacos"
    )
    nacos_client.set_options(default_timeout=15)
    cas_instance = None
    # nacos_client.add_naming_instance("cas.service", '127.0.0.1', 5000, 'casCluster', 0.1, "{}", False, True)
    nacos_client.add_naming_instance("cas.service", '127.0.0.1', 5000, 'casCluster')
    # nacos_client.add_naming_instance("cas.service", '127.0.0.1', 5000)
    try:
        cas_instance = nacos_client.get_naming_instance("cas.service", '127.0.0.1', 5000, 'casCluster')
        # cas_instance = nacos_client.get_naming_instance("cas.service", '127.0.0.1', 5000)
    except Exception as _:
        pass
    # print(nacos_client.get_naming_instance('cas.service', '127.0.0.1', 5000, 'casCluster'))
    if cas_instance is None:
        print("cas_instance is none")
    else:
        print(json.dumps(cas_instance, indent=2))
    cas_list = nacos_client.list_naming_instance("cas")
    print(json.dumps(cas_list, indent= 2))
    print(nacos_client.get_server())


if __name__ == '__main__':
    _main()
