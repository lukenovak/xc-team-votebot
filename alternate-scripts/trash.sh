while true
do
    while [ `jobs | wc -l` -ge 50 ] 
    do 
        echo 'waiting to spawn more processes'
        sleep 1 
    done

    curl 'https://nuhuskies.com/services/get_polls.ashx' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0' -H 'Accept: application/json, text/javascript, */*; q=0.01' --data 'poll_id=11&answer=WXC+-+Louiza+Wise' &
done
