B
    ?��^�
  �               @   s�   G d d� d�Z G dd� d�Ze� Ze�d� e�d� e�d� e�dd� e�d	� e�d
� e�d� e�d� ee�� � dS )c               @   s   e Zd Zdd� ZdS )�Nodec             C   s   || _ d | _d S )N)�value�next)�self�val� r   �e/Users/ratnamdubey/Documents/GitHub/DataStructures/Implementaions /Singly_LinkedList_Implementaion.py�__init__   s    zNode.__init__N)�__name__�
__module__�__qualname__r   r   r   r   r   r   
   s   r   c               @   s4   e Zd Zdd� Zdd� Zdd� Zdd� Zd	d
� ZdS )�Singly_Link_listc             C   s
   d | _ d S )N)�head)r   r   r   r   r      s    zSingly_Link_list.__init__c             C   s@   t |�}| jd kr|| _n"| j}x|jd kr4|j}q"W ||_d S )N)r   r   r   )r   r   Znew_node_val�
temp_pointr   r   r   �insert   s    

zSingly_Link_list.insertc             C   sR   t |�}| jd kr|| _n4| j}d}x||kr>|d }|j}q&W |j|_||_d S )N�    �   )r   r   r   )r   r   ZpositionZnew_valr   Ztemp_positionr   r   r   �append(   s    


zSingly_Link_list.appendc             C   sx   |dkr"| j d krdS | j j| _ nR|d }d}| j }x4||krh|j}t| j j� t| j jj� |d }q6W |jj|_d S )NZHeadzErrror Head node is Emptyr   r   )r   r   �printr   )r   r   �posr   r   r   r   �Delete8   s    

zSingly_Link_list.Deletec             C   s0   g }x&| j d kr*|�| j j� | j j| _ qW |S )N)r   r   r   r   )r   �ar   r   r   �	view_listM   s
    zSingly_Link_list.view_listN)r	   r
   r   r   r   r   r   r   r   r   r   r   r      s
   r   �
   �   �2   �   r   �   �7   �<   �A   N)r   r   �sr   r   r   r   r   r   r   r   r   �<module>
   s   H






