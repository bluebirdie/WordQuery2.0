#-*- coding:utf-8 -*-
import re
import random

from aqt.utils import showInfo, showText
from base import MdxService, export, register, with_styles

path = u'/home/victor/LDOCE6/L6mp3.mdx'
#path = u'/home/victor/ldoce6/LDOCE6.mdx'

@register(u'Local-LDOCE6')
class Ldoce6(MdxService):

    def __init__(self, dict_path):
        super(Ldoce6, self).__init__(path)

    @property
    def unique(self):
        return self.__class__.__name__

    @property
    def title(self):
        return self.__register_label__

    @export(u'Phonetic Alphabet', 1)
    def fld_phonetic(self):
        html = self.get_html()
        m = re.search(r'<span class="pron">(.*?)</span>', html)
        if m:
            return '/'+m.groups()[0]+'/'

    @export(u'British Audio', 2)
    def fld_voicebre(self):
        html = self.get_html()
        m = re.search(r'<span class="brevoice">(.*?)</span brevoice>', html)
        if m:
            return m.groups()[0]
        return ''

    @export(u'American Audio', 3)
    def fld_voiceame(self):
        html = self.get_html()
        m = re.search(r'<span class="amevoice">(.*?)</span amevoice>', html)
        if m:
            return m.groups()[0]
        return ''

    @export(u'POS', 4)
    def fld_pos(self):
        html = self.get_html()
        m = re.search(r'<span class="pos">(.*?)</span>', html)
        if m:
            return m.groups()[0]

    @export(u'Definition', 5)
    def fld_definate(self):
        html = self.get_html()
        m = re.search(r'<span class="def">(.*?)</span def>', html)
        if m:
            return m.groups()[0]
        return ''

    @export(u'First sentence', 6)
    def fld_sentence(self):
        html = self.get_html()
        m = re.search(r'<span class="example">(.*?)</span example>', html)
        if m:
            return re.sub('<img.*?png">', '', m.groups()[0])
        return ''

    @export(u'First 2 sentence audio', 7)
    def fld_first2sentence_audio(self):
        html = self.get_html()
        m = re.findall(
            r'(<span class="example">.+?</span example>)', html)
        if m:
            if len(m) == 1:
               return re.sub('<img.*?example>','', m[0])
            else:
               return re.sub('<img.*?example>','', m[0]) + '<br>' + re.sub('<img.*?example>','', m[1])
        return ''

    @export(u'First 2 sentence', 8)
    def fld_first2sentence(self):
        html = self.get_html()
        m = re.findall(
            r'(<span class="example">.+?</span example>)', html)
        if m:
            if len(m) == 1:
			   return re.sub('\[.*?png">','1.', m[0])
            else:
			   return re.sub('\[.*?png">','1.', m[0])+ '<br>' + re.sub('\[.*?png">','2.', m[1])
        return ''








 
