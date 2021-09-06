from kazoo.client import KazooClient
from kazoo import exceptions


class ZkApi(object):
    def __init__(self, zk_hosts):
        """
        链接zk的api类
        :param zk_hosts: zk的ip和端口号
        """
        self.zk_hosts = zk_hosts
        self.base_dir = '/EntAppFrameWorkconfig'

    def upload_zk_text(self, node_name, input_text):
        """
        :param node_name: zk的节点的名字
        :param input_text: 要向节点中插入的文本
        上传文本到zk
        :return:
        """
        zk_obj = KazooClient(hosts=self.zk_hosts)
        zk_obj.start()
        zk_obj.ensure_path(self.base_dir)
        # 创建或者写入节点
        try:
            zk_obj.create(self.base_dir + '/{}'.format(node_name), b" ")
            zk_obj.set(self.base_dir + '/{}'.format(node_name), input_text.encode('utf-8'))
        except exceptions.NodeExistsError:
            zk_obj.set(self.base_dir + '/{}'.format(node_name), input_text.encode('utf-8'))
        zk_obj.stop()
        return True


# bar = ZkApi(zk_hosts='192.168.0.222:22181', node_name='test', input_text='text')
# bar.upload_zk_text()
