/*
obtain the virtual image of an instance
*/

select i.id as instanceId, i.name as instanceName, vi.id as imageId, vi.name as imageName from instance i inner join instance_type_layout_container_type_set ic inner join container_type_set cts inner join container_type ct inner join virtual_image vi where i.layout_id = ic.instance_type_layout_containers_id and ic.container_type_set_id = cts.id and cts.container_type_id = ct.id and ct.virtual_image_id = vi.id and i.id = 2;