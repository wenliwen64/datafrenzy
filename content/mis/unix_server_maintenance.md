Titile: Unix Server Maintenance
Date: 2016-02-05 11:36
Slug: unix-server-maintenance
Authors: Liwen Wen

# Tips
- - -
* `e2label /dev/sda DISK_YUAN` to label filesystems and in `/etc/fstab`, you can add entry like `LABEL=DISK_YUAN /media/Disk_Yuan ext4 auto,rw 0 0  ` to automatically  mount filesystems. 

* `fdisk -l` shows all of the accessible filesystems on this computer
# Log:
- - -
* 2016-02-05
   
     1. `e2label/dev/mapper/fedora-home OLD_HOME` this disk actually is the new bought one(3T), but it shows several bad sectors at very beginning, add this entry using label to `/etc/fstab`
