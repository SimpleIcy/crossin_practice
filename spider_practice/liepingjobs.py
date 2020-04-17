from bs4 import BeautifulSoup
import requests
from typing import List, Any, Union
from time import sleep
import csv


class LiePingJobs:
    """
    猎聘职位信息抓取并保存到CSV文件。
    :arg
    """

    def __init__(self):
        self.req_home_url = 'https://www.liepin.com/zhaopin/?isAnalysis=&dqs=280020&pubTime=&salary=*&subIndustry=&industryType=&compscale=&key=python&init=-1&searchType=1&headckid=6dbfe75fcd81478e&flushckid=1&compkind=&fromSearchBtn=2&sortFlag=15&ckid=6dbfe75fcd81478e&jobKind=&industries=&clean_condition=&siTag=I-7rQ0e90mv8a37po7dV3Q%7EHjSmCnkUpSjgS7HPdUS6mw&d_sfrom=search_prime&d_ckId=2892ea505e6f8c2b57b1ee7e7d200057&d_curPage=0&d_pageSize=40&d_headId=2892ea505e6f8c2b57b1ee7e7d200057'
        self.req_next_url = 'https://www.liepin.com/zhaopin/?isAnalysis=&dqs=280020&pubTime=&salary=*&subIndustry=&industryType=&compscale=&key=python&init=-1&searchType=1&headckid=6dbfe75fcd81478e&compkind=&fromSearchBtn=2&sortFlag=15&ckid=76ca52c54da9386d&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=I-7rQ0e90mv8a37po7dV3Q%7EVcqkJLQTxDBNhgBNLLkbQg&d_sfrom=search_prime&d_ckId=f4232a221f903ea2d5ecad7cd41ce48e&d_curPage=0&d_pageSize=40&d_headId=2892ea505e6f8c2b57b1ee7e7d200057&curPage='
        self.headers = {'Sec-Fetch-Dest': 'document', 'Content-Type': 'text/html;charset=UTF-8', 'Connection': 'keep-alive', 'Host': 'www.liepin.com',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) '
                                      'Chrome/78.0.3904.97 Safari/537.36', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'same-origin',
                        'Cookie': '__uuid=1586068369907.70; fe_se=-1586068376589; __tlog=1586068369909.60%7C00000000%7CR000000075%7C00000000%7C00000000; Hm_lvt_a2647413544f5a04f00da7eee0d5e200=1586668021; Hm_lpvt_a2647413544f5a04f00da7eee0d5e200=1586668024; abtest=0; __session_seq=37; __uv_seq=2; JSESSIONID=2F5205D933321B824D11A506E5FD935D; __s_bid=2eccda464ca9d4e496919a907a364dbabc3e'}
        self.title = ['职位title', '职位详情url', '薪资', '城市', '学历要求', '职位年限要求', '职位发布时间', '反馈时间', '招聘公司', '公司业务所在行业', '公司福利'] # , '职位描述', '公司简介'

    def get_save_data(self, pages):
        for page in range(pages):
            if page >= 1:
                try:
                    req = requests.get(self.req_next_url + str(page), headers=self.headers)
                    print(self.req_next_url + str(page))
                except:
                    print('抓取第%s页时，网络requests请求异常！' % page)
                    continue
            else:
                try:
                    req = requests.get(self.req_home_url, headers=self.headers)
                    print(self.req_home_url)
                except:
                    print('抓取首页时，网络requests请求异常！')
                    break
            soup = BeautifulSoup(req.text, features="lxml")
            # page_data: bs4.element.Tag 对象组成的 list
            page_data = soup.select('ul[class="sojob-list"]')[0].select('li')
            print('length: %s' % len(page_data))
            for job in range(len(page_data)):
                # 需要抓取的招聘信息
                job_data: List[Union[str, Any]] = []
                # 职位title  type: string
                job_title = page_data[job].select('a')[0].string.replace('\r', '').replace('\t', '').replace('\n', '')
                job_data.append(job_title)
                # 职位详情url  type: string
                job_detail_url = page_data[job].select('a')[0].get_attribute_list('href')[0]
                if 'http' not in job_detail_url:
                    job_detail_url = 'https://www.liepin.com' + job_detail_url
                job_data.append(job_detail_url)
                # 薪资：   type: string
                salary = page_data[job].select('.text-warning')[0].string
                job_data.append(salary)
                # 城市  example 成都  type: string
                city = page_data[job].select('.area')[0].string
                job_data.append(city)
                # 学历要求 example 本科及以上  type: string
                edu_required = page_data[job].select('.edu')[0].string
                job_data.append(edu_required)
                # 职位年限要求  example 3年以上  type: string
                years_required = page_data[job].select('p')[0].getText().strip().split('\n')[-1]
                job_data.append(years_required)
                # 职位发布时间  example 前天   type: string
                job_pub_time = page_data[job].select('time')[0].string
                job_data.append(job_pub_time)
                # 反馈时间 example '投递后：5个工作日内反馈' type: string
                try:
                    feed_within_time = page_data[job].select('p')[1].select('span')[0].string
                    job_data.append(feed_within_time)
                except IndexError:
                    job_data.append('未录入')
                # 招聘公司名称  type: string
                corp_name = page_data[job].select('.company-name')[0].get_text().strip()
                job_data.append(corp_name)
                # 公司业务所在行业或融资规模  type: string  互联网+
                try:
                    corp_industry = page_data[job].select('.industry-link')[0].get_text().strip().replace('\r', '').replace('\t', '').replace('\n', '')
                    job_data.append(corp_industry)
                except IndexError:
                    try:
                        field_financing = page_data[job].select('.field-financing')[0].select('span')[0].string.replace('\r', '').replace('\t', '').replace('\n', '')
                        job_data.append(field_financing)
                    except IndexError:
                        job_data.append('None')
                # 公司福利  type: string
                try:
                    corp_welfare = page_data[job].select('.temptation.clearfix')[0].get_text().strip().replace('\r', '').replace('\t', '').replace('\n', '')
                    job_data.append(corp_welfare)
                except IndexError:
                    job_data.append('未录入')
                print(job_data)
                # # 职位描述
                # req_second = requests.get(job_detail_url, headers=self.headers)
                # soup_second = BeautifulSoup(req_second.text, features="lxml")
                # job_detail_require = soup_second.select('.content.content-word')[0].get_text()
                # job_data.append(job_detail_require)
                # 公司简介
                # corp_info = soup_second.select('.info-word')[0].get_text().strip()
                # job_data.append(corp_info)
                # 此条招聘数据写入csv文件。
                with open('ChengDuPythonHire.csv', 'a+', encoding='utf-8', newline='') as f:
                    f_csv = csv.writer(f)
                    f_csv.writerow(job_data)
            # 请求间隔5秒防止被网站屏蔽
            sleep(3)

    def save_data_header(self):
        with open('ChengDuPythonHire.csv', 'a+', encoding='utf-8', newline='') as f:
            f_csv = csv.writer(f)
            f_csv.writerow(self.title)


if __name__ == '__main__':
    Hire = LiePingJobs()
    Hire.save_data_header()
    Hire.get_save_data(10)
